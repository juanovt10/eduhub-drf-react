from django.db.models import Count, Sum
from django.http import Http404
from rest_framework import status, permissions, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Course, COURSE_CATEGORIES
from .serializers import CourseSerializer
from eduhub_drf_api.permissions import IsOwnerOrReadOnly


class CourseList(generics.ListCreateAPIView):
    serializer_class = CourseSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Course.objects.annotate(
        ratings_count = Count('rating', distinct=True),
        enrollments_count = Count('enrollment', distinct=True),
        overall_rating = (Sum('rating__rating')) / Count('rating', distinct=True),
    ).order_by('created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner',
        'categories',
    ]
    search_fields = [
        'owner__username',
        'title',
        'categories',
    ]
    ordering_fields = [
        'ratings_count',
        'enrollment_count',
        'created_at', 
        'price',
        'duration',
        'created_at',
    ]



    def create(self, request, *args, **kwargs):
        if not request.user.profile.is_instructor:
            return Response(
                {'detail': 'You do not have permission to create a course. Only certified instructors can create courses.'},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().create(request, *args, **kwargs)

class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CourseSerializer
    queryset = Course.objects.annotate(
        ratings_count = Count('rating', distinct=True),
        enrollments_count = Count('enrollment', distinct=True),
        overall_rating = (Sum('rating__rating')) / Count('rating', distinct=True),
    ).order_by('created_at')

class CourseCategoryList(APIView):
    def get(self, request, format=None):
        categories = [{'key': cat[0], 'value': cat[1]} for cat in COURSE_CATEGORIES]
        return Response(categories)



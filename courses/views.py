from django.db.models import Count
from django.http import Http404
from rest_framework import status, permissions, generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Course
from .serializers import CourseSerializer
from eduhub_drf_api.permissions import IsOwnerOrReadOnly


class CourseList(generics.ListAPIView):
    serializer_class = CourseSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Course.objects.annotate(
        ratings_count = Count('rating', distinct=True),
        enrollments_count = Count('enrollment', distinct=True),
    ).order_by('created_at')
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'ratings_count',
        'enrollment_count',
        'created_at', 
        'price',
        'duration',
        'created_at',
    ]


class CourseDetail(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CourseSerializer
    queryset = Course.objects.annotate(
        ratings_count = Count('rating', distinct=True),
        enrollments_count = Count('enrollment', distinct=True),
    ).order_by('created_at')

    def get_object(self, pk):
        try:
            course = Course.objects.annotate(
                ratings_count = Count('rating', distinct=True),
                enrollments_count = Count('enrollment', distinct=True),
            ).get(pk=pk)
            self.check_object_permissions(self.request, course)
            return course
        except Course.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        course = self.get_object(pk)
        serializer = CourseSerializer(
            course, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        course = self.get_object(pk)
        serializer = CourseSerializer(
            course, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        course = self.get_object(pk)
        course.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )



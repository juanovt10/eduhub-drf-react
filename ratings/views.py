from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from eduhub_drf_api.permissions import IsOwnerOrReadOnly
from django.db.models import Count
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Rating
from .serializers import RatingSerializer, RatingDetailSerializer


class RatingList(generics.ListCreateAPIView):
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Rating.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['owner', 'course', 'rating']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
    permissio_classes = [IsOwnerOrReadOnly]
    serializer_class = RatingDetailSerializer
    queryset = Rating.objects.all()


class RatingStatsView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request, course_id):
        data = (Rating.objects
                .filter(course_id=course_id)
                .values('rating')
                .annotate(count=Count('id'))
                .order_by('rating'))

        return Response(data)

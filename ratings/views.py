from rest_framework import generics, permissions
from eduhub_drf_api.permissions import IsOwnerOrReadOnly
from .models import Rating
from .serializers import RatingSerializer, RatingDetailSerializer


class RatingList(generics.ListCreateAPIView):
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Rating.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
    permissio_classes = [IsOwnerOrReadOnly]
    serializer_class = RatingDetailSerializer
    queryset = Rating.objects.all()







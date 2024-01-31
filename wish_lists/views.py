from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from eduhub_drf_api.permissions import IsOwnerOrReadOnly
from .models import WishList
from .serializers import WishListSerializer


class WishListList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = WishListSerializer
    queryset = WishList.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['course']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class WishListDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = WishListSerializer
    queryset = WishList.objects.all()


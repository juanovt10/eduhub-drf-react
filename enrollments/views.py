from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from eduhub_drf_api.permissions import IsOwnerOrReadOnly
from .models import Enrollment
from .serializers import EnrollmentSerializer


class EnrollmentList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = EnrollmentSerializer
    queryset = Enrollment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['course']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EnrollmentDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = EnrollmentSerializer
    queryset = Enrollment.objects.all()


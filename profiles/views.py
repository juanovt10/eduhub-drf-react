from django.db.models import Count
from rest_framework import generics, filters, status, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from .models import Profile, InstructorApplication
from .serializers import ProfileSerializer, InstructorApplicationSerializer
from eduhub_drf_api.permissions import IsOwnerOrReadOnly



class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.annotate(
        ratings_count = Count('owner__rating', distinct=True),
        enrollments_count = Count('owner__enrollment', distinct=True),
        wish_list_count = Count('owner__wishlist', distinct=True),
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend
    ]
    filterset_fields = [
        'owner',
        'is_instructor',
    ]
    ordering_fields = [
        'ratings_count',
        'enrollments_count',
        'wish_list_count',
        'created_at',
    ]


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        ratings_count = Count('owner__rating', distinct=True),
        enrollments_count = Count('owner__enrollment', distinct=True),
        wish_list_count = Count('owner__wishlist', distinct=True),
    ).order_by('-created_at')

    def delete(self, request, *args, **kwargs):
        profile = self.get_object()
        user = get_object_or_404(User, id=profile.owner.id)

        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class InstructorApplicationCreateView(generics.ListCreateAPIView):
    queryset = InstructorApplication.objects.all()
    serializer_class = InstructorApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()  
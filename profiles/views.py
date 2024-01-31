from django.db.models import Count
from rest_framework import generics, filters
from .models import Profile
from .serializers import ProfileSerializer
from eduhub_drf_api.permissions import IsOwnerOrReadOnly



class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.annotate(
        ratings_count = Count('owner__rating', distinct=True),
        enrollments_count = Count('owner__enrollment', distinct=True),
        wish_list_count = Count('owner__wishlist', distinct=True),
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'ratings_count',
        'enrollments_count',
        'wish_list_count',
        'created_at',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        ratings_count = Count('owner__rating', distinct=True),
        enrollments_count = Count('owner__enrollment', distinct=True),
        wish_list_count = Count('owner__wishlist', distinct=True),
    ).order_by('-created_at')

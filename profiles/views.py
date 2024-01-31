from rest_framework import generics, filters
from .models import Profile
from .serializers import ProfileSerializer
from eduhub_drf_api.permissions import IsOwnerOrReadOnly



class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()

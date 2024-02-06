from rest_framework import serializers 
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    ratings_count = serializers.ReadOnlyField()
    enrollments_count = serializers.ReadOnlyField()
    wish_list_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'name', 'bio',
            'image', 'dob', 'is_owner', 'is_instructor',
            'ratings_count', 'enrollments_count', 
            'wish_list_count',
        ]
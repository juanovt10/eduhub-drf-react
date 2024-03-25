from rest_framework import serializers 
from .models import Profile, InstructorApplication


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    ratings_count = serializers.ReadOnlyField()
    enrollments_count = serializers.ReadOnlyField()
    wish_list_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
        
    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size larger than 2MB'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px'
            )


    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'name', 'bio',
            'image', 'dob', 'is_owner', 'is_instructor',
            'ratings_count', 'enrollments_count', 
            'wish_list_count',
        ]

class InstructorApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstructorApplication
        fields = ['id', 'application_text', 'applied_on']
        read_only_fields = ['id', 'applied_on', 'approved']

    def create(self, validated_data):
        if InstructorApplication.objects.filter(owner=user).exists():
            raise ValidationError('An application already exist for this user')
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)

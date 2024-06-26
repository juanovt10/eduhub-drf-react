from rest_framework import serializers
from .models import Course
from ratings.models import Rating


class CourseSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(
        source='owner.profile.id'
    )
    profile_image = serializers.ReadOnlyField(
        source='owner.profile.image.url'
    )
    rating_id = serializers.SerializerMethodField()
    ratings_count = serializers.ReadOnlyField()
    enrollments_count = serializers.ReadOnlyField()
    overall_rating = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_rating_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            rating = Rating.objects.filter(
                owner=user, course=obj
            ).first()
            return rating.id if rating else None
        return None

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

        return value

    class Meta:
        model = Course
        fields = [
            'id', 'title', 'description', 'owner', 'image',
            'category', 'created_at', 'price',
            'video_hours', 'test_count', 'article_count',
            'is_owner', 'profile_id', 'overall_rating',
            'profile_image', 'rating_id', 'ratings_count',
            'enrollments_count',
        ]

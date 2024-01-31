from django.db import IntegrityError
from rest_framework import serializers
from .models import WishList


class WishListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = WishList
        fields = ['id', 'owner', 'course', 'added_at']

    def create(self, validated_data):
        try: 
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
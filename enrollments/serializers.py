from django.db import IntegrityError
from rest_framework import serializers
from .models import Enrollment


class EnrollmentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Enrollment
        fields = ['id', 'owner', 'course', 'enrolled_at', 'completed']

    def create(self, validated_data):
        try: 
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
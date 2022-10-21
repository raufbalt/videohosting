from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    material = serializers.ReadOnlyField(source='material.title')

    class Meta:
        model = Review
        fields = "__all__"

from rest_framework import serializers

from rating.serializers import ReviewSerializer
from .models import Category, Material


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class MaterialListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Material
        fields = ('title', 'year', 'category')


class MaterialDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Material
        fields = ('title', 'year', 'desc')

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['rating'] = ReviewSerializer(instance.reviews.all(), many=True).data
        return repr


class MaterialCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Material
        fields = ('title', 'year', 'video', 'desc', 'image', 'category')


from rest_framework import serializers

from favorites.models import Favorite


class FavoriteListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorite
        fields = ('materials',)


class FavoriteDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorite
        fields = '__all__'


class FavoriteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('materials',)

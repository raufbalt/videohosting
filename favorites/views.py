from django.shortcuts import render
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from favorites.models import Favorite
from . import serializers


class FavoriteViewSet(ModelViewSet):
    queryset = Favorite.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.FavoriteListSerializer
        if self.action == 'POST':
            return serializers.FavoriteCreateSerializer
        return serializers.FavoriteDetailSerializer

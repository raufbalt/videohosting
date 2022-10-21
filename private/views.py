from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from private.models import Private
from . import serializers, permissions


class PrivateViewSet(ModelViewSet):
    queryset = Private.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.PrivateListSerializer
        if self.action == 'POST':
            return serializers.PrivateCreateSerializer
        return serializers.PrivateDetailSerializer

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return [permissions.IsAdminUser()]
        return [permissions.IsPrivateUser()]


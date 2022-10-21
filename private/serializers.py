from rest_framework import serializers

from private.models import Private


class PrivateListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Private
        fields = ('title', 'year')


class PrivateDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Private
        fields = ('title', 'year', 'desc')


class PrivateCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Private
        fields = ('title', 'year', 'video', 'desc', 'image',)

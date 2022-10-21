from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination

from rest_framework import permissions, response
from rest_framework.viewsets import ModelViewSet

from rating.serializers import ReviewSerializer
from . import serializers

from material.models import Category, Material
from .serializers import CategorySerializer


class StandartResultsPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'page'
    max_page_size = 1000


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.action == 'POST':
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]


class MaterialViewSet(ModelViewSet):
    queryset = Material.objects.all()
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('title',)
    filterset_fields = ('category', )
    pagination_class = StandartResultsPagination

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.MaterialListSerializer
        if self.action == 'POST':
            return serializers.MaterialCreateSerializer
        return serializers.MaterialDetailSerializer

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticatedOrReadOnly()]

    @action(['GET', 'POST'], detail=True)
    def reviews(self, request, pk):
        material = self.get_object()
        if request.method == 'GET':
            reviews = material.reviews.all()
            serializer = ReviewSerializer(reviews, many=True)
            return response.Response(serializer.data, status=200)
        if material.reviews.filter(owner=request.user).exists():
            return response.Response('Вы уже оставляли отзыв', status=400)
        data = request.data
        serializer = ReviewSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user, material=material)
        return response.Response(serializer.data, status=201)
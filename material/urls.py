from django.urls import path, include

from .views import MaterialViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('material', MaterialViewSet)

urlpatterns = [
    path('', include(router.urls))
]
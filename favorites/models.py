from django.db import models
from django.contrib.auth import get_user_model

from material.models import Material

User = get_user_model()


class Favorite(models.Model):

    materials = models.ForeignKey(Material, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Favorite'
        verbose_name_plural = 'Favorites'

    def __str__(self):
        return self.owner




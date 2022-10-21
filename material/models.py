from django.db import models
from django.core import validators


class Material(models.Model):
    title = models.CharField(max_length=30, unique=True)
    year = models.SmallIntegerField(blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='media/', blank=True)
    video = models.FileField(upload_to='media/', blank=True, validators=[validators.FileExtensionValidator(['mp4'], message='file must be mp3')])

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=30, unique=True, verbose_name='Category')
    image = models.ImageField(upload_to='media/', blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


    def __str__(self):
        return self.title




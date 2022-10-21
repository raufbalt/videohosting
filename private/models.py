from django.db import models
from django.core import validators


class Private(models.Model):
    title = models.CharField(max_length=30, unique=True)
    year = models.SmallIntegerField(blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='media/', blank=True)
    video = models.FileField(upload_to='media/', blank=True, validators=[validators.FileExtensionValidator(['mp4'], message='file must be mp3')])

    def __str__(self):
        return self.title

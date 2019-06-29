from django.db import models
from django.conf import settings


class Article(models.Model):
    headline = models.CharField(max_length=120)
    trailtext = models.CharField(max_length=120)
    thumbnail = models.URLField()
    url = models.URLField()
    date = models.CharField(max_length=120)
    source = models.CharField(max_length=120)

    def __str__(self):
        return self.headline

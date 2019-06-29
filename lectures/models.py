from django.db import models

class Lecture(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    given_by = models.CharField(max_length=100)
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text

from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=50)
    show_time = models.CharField(max_length=30)
    type = models.CharField(max_length=30)

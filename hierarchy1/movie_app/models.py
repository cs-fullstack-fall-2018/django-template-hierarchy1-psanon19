from django.db import models


class MovieModel(models.Model):
    name = models.CharField(max_length=100)
    yearReleased = models.IntegerField(default=0)
    rating = models.CharField(max_length=1)
    genre = models.CharField(max_length=200)
    summary = models.TextField(max_length=500)
    pic_url = models.URLField(null='true')

    def __str__(self):
        return self.name

from django.db import models


class Series(models.Model):

    name = models.CharField(max_length=200)
    image = models.CharField(max_length=500)
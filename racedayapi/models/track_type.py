from django.db import models


class Track_Type(models.Model):

    label = models.CharField(max_length=150)
from django.db import models
from django.contrib.auth.models import User


class Track(models.Model):

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="Users")
    tracktype = models.ForeignKey("Track_Type", on_delete=models.CASCADE, related_name="Types")
    name = models.CharField(max_length=300)
    location = models.CharField(max_length=150)
    length = models.CharField(max_length=100)
    turns = models.CharField(max_length=2)
    seating_capacity = models.CharField(max_length=100)
    image = models.CharField(max_length=500)

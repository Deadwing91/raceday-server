from django.db import models
from django.contrib.auth.models import User


class Track(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    track_typeId = models.ForeignKey("Track_Type", on_delete=models.CASCADE, related_name="Types")
    name = models.CharField(max_length=300)
    location = models.CharField(max_length=150)
    image = models.ImageField()
    bio = models.CharField(max_length=300)

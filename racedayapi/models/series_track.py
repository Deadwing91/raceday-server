from django.db import models


class Series_Track(models.Model):

    series = models.ForeignKey("Series", on_delete=models.DO_NOTHING, related_name="Series_Relationships")
    track = models.ForeignKey("Track", on_delete=models.CASCADE, related_name="Track_Relationships")
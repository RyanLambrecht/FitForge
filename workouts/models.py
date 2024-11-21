from django.db import models
from accounts.models import CustomUser
from django.conf import settings


class LiftingWorkout(models.Model):
    name = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    date = models.DateField()
    exercise = models.CharField(max_length=50)
    weight = models.IntegerField()
    reps = models.IntegerField()
    sets = models.IntegerField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name.username, self.date, self.exercise}"


class CardioWorkout(models.Model):
    name = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    date = models.DateField()
    exercise = models.CharField(max_length=50)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    distance = models.FloatField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name.username, self.date, self.exercise}"

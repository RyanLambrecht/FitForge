from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import User

FITNESS_LEVELS = (
    (1, "Beginner"),
    (2, "Intermediate"),
    (3, "Advanced"),
)

GENDERS = (
    (1, "Male"),
    (2, "Female"),
)


class CustomUser(AbstractUser):
    username = models.CharField(max_length=40, null="", blank=False, unique=True)
    first_name = models.CharField(max_length=40, null="", blank=False)
    last_name = models.CharField(max_length=40, null="", blank=False)
    age = models.PositiveIntegerField(null=False, blank=False)
    weight = models.PositiveIntegerField(null=False, blank=False)
    fitness_level = models.IntegerField(choices=FITNESS_LEVELS)
    gender = models.IntegerField(choices=GENDERS)
    groups = models.ManyToManyField(blank=True, to="auth.group")
    user_permissions = models.ManyToManyField(blank=True, to="auth.permission")

    def __str__(self):
        return f"{self.first_name}"

# checkin model
class DailyCheckIn(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    workout_completed = models.TextField(blank=True, null=True)
    meals = models.TextField(blank=True, null=True)
    progress_notes = models.TextField(blank=True, null=True)

    class Meta:
        # one per day
        unique_together = ('user', 'date')  

    def __str__(self):
        return f"{self.user.username} - {self.date}"
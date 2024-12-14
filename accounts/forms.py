from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser
from .models import DailyCheckIn


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "age",
            "height_FT",
            "height_IN",
            "weight",
            "fitness_level",
            "gender",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "age",
            "height_FT",
            "height_IN",
            "weight",
            "fitness_level",
            "gender",
        )

    


# form for checkin
class DailyCheckInForm(forms.ModelForm):
    class Meta:
        model = DailyCheckIn
        fields = ["workout_completed", "meals", "progress_notes"]

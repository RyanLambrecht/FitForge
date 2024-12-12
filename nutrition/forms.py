from django import forms
from .models import Food


class CaloricIntakeForm(forms.Form):
    caloric_intake = forms.IntegerField(label="Caloric Intake (kcal)", min_value=1000)


class DailyMacroForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = [
            "date",
            "calories",
            "protein",
            "carbs",
            "fats",
        ]


class FoodIntakeForm(forms.Form):
    food_intake = forms.CharField(max_length=10000)

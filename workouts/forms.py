from django import forms
from .models import CardioWorkout, LiftingWorkout


class AddCardio(forms.ModelForm):
    class Meta:
        model = CardioWorkout
        fields = [
            "name",
            "date",
            "exercise",
            "start_time",
            "end_time",
            "distance",
            "notes",
        ]


class EditCardio(forms.ModelForm):
    class Meta:
        model = CardioWorkout
        fields = [
            "date",
            "exercise",
            "start_time",
            "end_time",
            "distance",
            "notes",
        ]


class AddLift(forms.ModelForm):
    class Meta:
        model = LiftingWorkout
        fields = [
            "date",
            "exercise",
            "weight",
            "reps",
            "sets",
            "notes",
        ]


class EditLift(forms.ModelForm):
    class Meta:
        model = LiftingWorkout
        fields = [
            "date",
            "exercise",
            "weight",
            "reps",
            "sets",
            "notes",
        ]

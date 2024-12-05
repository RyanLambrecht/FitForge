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

class TargetSearch(forms.Form):
    MUSCLE_OPTIONS = [
        ('abs', 'Abs'),
        ('biceps', 'Biceps'),
        ('calves', 'Calves'),
        ('cardiovascular system', 'Cardiovascular'),
        ('delts', 'Delts'),
        ('forearms', 'Forearms'),
        ('glutes', 'Glutes'),
        ('hamstrings', 'Hamstrings'),
        ('lats', 'Lats'),
        ('levator scapulae', 'Levator Scapulae'),
        ('pectorals', 'Pectorals'),
        ('quads', 'Quads'),
        ('serratus anterior', 'Serratus Anterior'),
        ('spine', 'Spine'),
        ('traps', 'Traps'),
        ('triceps', 'Triceps'),
        ('upper back', 'Upper Back'),
    ]

    search_choice = forms.ChoiceField(choices=MUSCLE_OPTIONS)

class BodyPartSearch(forms.Form):
    BODY_PART_OPTIONS = [
        ('upper arms', 'Arms (Upper)'),
        ('lower arms', 'Arms (Lower)'),
        ('back', 'Back'),
        ('cardio', 'Cardio'),
        ('chest', 'Chest'),
        ('upper legs', 'Legs (Upper)'),
        ('lower legs', 'Legs (Lower)'),
        ('neck', 'Neck'),
        ('shoulders', 'Shoulders'),
        ('waist', 'Waist'),
    ]

    search_choice = forms.ChoiceField(choices=BODY_PART_OPTIONS)
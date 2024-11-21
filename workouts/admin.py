from django.contrib import admin
from .models import CardioWorkout, LiftingWorkout
from .forms import AddCardio, EditCardio, AddLift, EditLift


class CardioAdmin(admin.ModelAdmin):
    add_form = AddCardio
    form = EditCardio
    list_display = [
        "name",
        "date",
        "exercise",
        "start_time",
        "end_time",
        "distance",
        "notes",
    ]

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "date",
                    "exercise",
                    "start_time",
                    "end_time",
                    "distance",
                    "notes",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "date",
                    "exercise",
                    "start_time",
                    "end_time",
                    "distance",
                    "notes",
                )
            },
        ),
    )


class LiftingAdmin(admin.ModelAdmin):
    add_form = AddLift
    form = EditLift
    list_display = [
        "name",
        "date",
        "exercise",
        "weight",
        "reps",
        "sets",
        "notes",
    ]

    fieldsets = (
        (
            None,
            {"fields": ("name", "date", "exercise", "weight", "reps", "sets", "notes")},
        ),
    )
    add_fieldsets = (
        (
            None,
            {"fields": ("name", "date", "exercise", "weight", "reps", "sets", "notes")},
        ),
    )


admin.site.register(CardioWorkout, CardioAdmin)
admin.site.register(LiftingWorkout, LiftingAdmin)

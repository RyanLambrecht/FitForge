from django.contrib import admin
from .models import Food
from .forms import FoodIntakeForm


class FoodAdmin(admin.ModelAdmin):
    add_form = FoodIntakeForm
    list_display = [
        "name",
        "date",
        "calories",
        "protein",
        "carbs",
        "fats",
    ]

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "date",
                    "calories",
                    "protein",
                    "carbs",
                    "fats",
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
                    "calories",
                    "protein",
                    "carbs",
                    "fats",
                )
            },
        ),
    )


admin.site.register(Food, FoodAdmin)

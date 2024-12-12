from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "username",
        "first_name",
        "last_name",
        "email",
        "age",
        "height_FT",
        "height_IN",
        "weight",
        "gender",
        "fitness_level",
    ]

    fieldsets = UserAdmin.fieldsets + (
        (
            None,
            {
                "fields": (
                    "age",
                    "height_FT",
                    "height_IN",
                    "weight",
                    "gender",
                    "fitness_level",
                )
            },
        ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            None,
            {
                "fields": (
                    "age",
                    "height_FT",
                    "height_IN",
                    "weight",
                    "gender",
                    "fitness_level",
                )
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)

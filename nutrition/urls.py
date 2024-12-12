from django.urls import path
from .views import (
    set_caloric_intake,
    view_recommendations,
    DailyIntakeView,
    search_nutrients,
)

urlpatterns = [
    path("set-caloric-intake/", set_caloric_intake, name="set_caloric_intake"),
    # path('meal-suggestions/', views.meal_suggestions, name='meal_suggestions'),
    path("macro_recommendations/", view_recommendations, name="recommendations"),
    path("new_nutrient_input/", DailyIntakeView.as_view(), name="intake_form"),
    path("search/", search_nutrients, name="nutrient_search"),
]

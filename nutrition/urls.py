from django.urls import path
from .views import (
    set_caloric_intake,
    view_recommendations,
    DailyIntakeView,
    search_nutrients,
    edit_daily_intake
)

urlpatterns = [
    path("nutrition\daily_intake.html", set_caloric_intake, name="set_caloric_intake"),
    # path('meal-suggestions/', views.meal_suggestions, name='meal_suggestions'),
    path("nutrition\recommendations.html", view_recommendations, name="recommendations"),
    path("new_nutrient_input/", DailyIntakeView.as_view(), name="intake_form"),
    path("search/", search_nutrients, name="nutrient_search"),
    path('edit_daily_intake/<int:pk>/', edit_daily_intake, name='edit_daily_intake'),
]

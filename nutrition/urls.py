from django.urls import path
from . import views

urlpatterns = [
    path('set-caloric-intake/', views.set_caloric_intake, name='set_caloric_intake'),
    path('meal-suggestions/', views.meal_suggestions, name='meal_suggestions'),
]
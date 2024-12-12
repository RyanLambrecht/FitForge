from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CaloricIntakeForm, DailyMacroForm, FoodIntakeForm
from .models import Food
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, FormView
from django.urls import reverse_lazy
import requests
import os


@login_required
def set_caloric_intake(request):
    if request.method == "POST":
        form = CaloricIntakeForm(request.POST)
        if form.is_valid():
            request.user.caloric_intake = form.cleaned_data["caloric_intake"]
            request.user.save()
            return redirect("meal_suggestions")  # meal suggestions
    else:
        form = CaloricIntakeForm()
    return render(request, "nutrition/daily_intake.html", {"form": form})


@login_required
def view_recommendations(request):
    user = request.user

    bmi_url = f"https://nutrition-calculator.p.rapidapi.com/api/bmi"

    headers = {
        "x-rapidapi-key": os.getenv("RAPIDAPI_KEY"),
        "x-rapidapi-host": os.getenv("RAPIDAPI_HOST_MACROS"),
    }

    querystring = {
        "measurement_units": "std",
        "feet": user.height_FT,
        "inches": user.height_IN,
        "lbs": user.weight,
    }

    response_bmi = requests.get(bmi_url, headers=headers, params=querystring)
    data_bmi = response_bmi.json()

    macros_url = f"https://nutrition-calculator.p.rapidapi.com/api/nutrition-info"

    querystring = {
        "measurement_units": "std",
        "sex": "male",
        "age_value": user.age,
        "age_type": "yrs",
        "feet": user.height_FT,
        "inches": user.height_IN,
        "lbs": user.weight,
        "activity_level": user.fitness_level,
    }

    response_macros = requests.get(macros_url, headers=headers, params=querystring)
    data_macros = response_macros.json()

    bmi = data_macros["BMI_EER"]["BMI"]
    caloric_needs = data_macros["BMI_EER"]["Estimated Daily Caloric Needs"]

    macronutrients = data_macros["macronutrients_table"]["macronutrients-table"]
    minerals = data_macros["minerals_table"]["essential-minerals-table"]
    non_essential_minerals = data_macros["non_essential_minerals_table"][
        "non-essential-minerals-table"
    ]
    vitamins = data_macros["vitamins_table"]["vitamins-table"]

    context = {
        "bmi": bmi,
        "caloric_needs": caloric_needs,
        "macronutrients": macronutrients,
        "minerals": minerals,
        "non_essential_minerals": non_essential_minerals,
        "vitamins": vitamins,
        "user": user,
    }

    return render(request, "nutrition/recommendations.html", context)


class DailyIntakeView(LoginRequiredMixin, FormView):
    model = Food
    form_class = DailyMacroForm
    template_name = "nutrition/daily_intake.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.name = self.request.user
        form.save()
        return super().form_valid(form)


@login_required
def search_nutrients(request):
    if request.method == "GET":
        form = FoodIntakeForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data["food_intake"]

            url = f"https://edamam-edamam-nutrition-analysis.p.rapidapi.com/api/nutrition-data"

            querystring = {
                "nutrition-type": "cooking",
                "ingr": query,
            }

            headers = {
                "x-rapidapi-key": os.getenv("RAPIDAPI_KEY"),
                "x-rapidapi-host": os.getenv("RAPIDAPI_HOST_NUTRITIONDATA"),
            }

            response = requests.get(url, headers=headers, params=querystring)
            data = response.json()

            calories = data["calories"]
            diet_labels = data["dietLabels"]
            health_labels = data["healthLabels"]
            total_nutrients = data["totalNutrients"]

            context = {
                "calories": calories,
                "diet_labels": diet_labels,
                "health_labels": health_labels,
                "total_nutrients": total_nutrients,
            }

            return render(request, "nutrition/search_results_macros.html", context)

    else:
        form = FoodIntakeForm()

    return render(request, "nutrition/search_foods.html", {"form": form})

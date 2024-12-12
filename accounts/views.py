from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import DailyCheckIn, CustomUser
from .forms import DailyCheckInForm
from nutrition.forms import CaloricIntakeForm
from nutrition.models import Food


# Signup view
def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Signup successful")
            return redirect("home")
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


# Edit account view
@login_required
def edit_account_view(request, pk):
    user = CustomUser.objects.get(pk=pk)

    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CustomUserChangeForm(instance=user)

    return render(
        request, "registration/edit_account.html", {"form": form, "user": user}
    )


# Login view
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful")
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "registration/login.html", {"form": form})


# Home view
def home_view(request):
    return render(request, "pages/home.html")


# Daily check-in view
@login_required
def daily_checkin_view(request):
    today = timezone.now().date()
    checkin, created = DailyCheckIn.objects.get_or_create(user=request.user, date=today)
    if request.method == "POST":
        form = DailyCheckInForm(request.POST, instance=checkin)
        if form.is_valid():
            form.save()
            return redirect("progress_report")
    else:
        form = DailyCheckInForm(instance=checkin)

    return render(
        request, "checkins/daily_checkin.html", {"form": form, "today": today}
    )


# Progress report view
@login_required
def progress_report_view(request):
    checkins = DailyCheckIn.objects.filter(user=request.user).order_by("-date")
    return render(request, "checkins/progress_report.html", {"checkins": checkins})


# Set caloric intake view
@login_required
def set_caloric_intake_view(request):
    if request.method == "POST":
        form = CaloricIntakeForm(request.POST)
        if form.is_valid():
            request.user.caloric_intake = form.cleaned_data["caloric_intake"]
            request.user.save()
            messages.success(request, "Caloric intake updated successfully!")
            return redirect("meal_suggestions")  # redirect to meal suggestions
    else:
        form = CaloricIntakeForm()
    return render(request, "nutrition/set_caloric_intake.html", {"form": form})


# meal suggestions view
@login_required
def meal_suggestions_view(request):
    user = request.user
    caloric_intake = user.caloric_intake

    if caloric_intake is None:
        return redirect("set_caloric_intake")  # redirect to set caloric intae

    foods = Food.objects.all()
    suggestions = generate_meal_plan(foods, caloric_intake)

    return render(
        request, "nutrition/meal_suggestions.html", {"suggestions": suggestions}
    )


# generate a meal plan
def generate_meal_plan(foods, caloric_intake):
    suggestions = []
    current_calories = 0
    while current_calories < caloric_intake:
        food = foods.order_by("?").first()  # random
        if current_calories + food.calories <= caloric_intake:
            suggestions.append(food)
            current_calories += food.calories
    return suggestions

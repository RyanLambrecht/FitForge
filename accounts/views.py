from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.shortcuts import render
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.shortcuts import render, redirect
from .models import DailyCheckIn, CustomUser
from .forms import DailyCheckInForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils import timezone
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


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
            return redirect("home")  # Redirect to home page after login
    else:
        form = AuthenticationForm()
    return render(request, "registration/login.html", {"form": form})


def home_view(request):
    return render(request, "pages/home.html")


# login view for checkin feature
@login_required
def daily_checkin_view(request):
    today = timezone.now().date()
    checkin, created = DailyCheckIn.objects.get_or_create(user=request.user, date=today)
    if request.method == "POST":
        form = DailyCheckInForm(request.POST, instance=checkin)
        if form.is_valid():
            form.save()
            return redirect(
                "progress_report"
            )  # Redirect to progress report or dashboard
    else:
        form = DailyCheckInForm(instance=checkin)

    return render(
        request, "checkins/daily_checkin.html", {"form": form, "today": today}
    )


@login_required
def progress_report_view(request):
    checkins = DailyCheckIn.objects.filter(user=request.user).order_by("-date")
    return render(request, "checkins/progress_report.html", {"checkins": checkins})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "Logout successful")
    return redirect("home")

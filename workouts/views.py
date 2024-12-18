from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import LiftingWorkout, CardioWorkout
from .forms import (
    AddLift,
    EditLift,
    AddCardio,
    EditCardio,
    TargetSearch,
    BodyPartSearch,
    EquipmentSearch,
)
from nutrition.models import Food  # Adjust the import based on your actual model names
from django.views.generic import CreateView, FormView, TemplateView, ListView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import Http404
from functools import wraps
import requests
import os

# workouts/views.py

def home_view(request):
    if request.user.is_authenticated:
        cardio_workouts = CardioWorkout.objects.filter(name=request.user).order_by('-date')
        lifting_workouts = LiftingWorkout.objects.filter(name=request.user).order_by('-date')
        nutrition_plans = Food.objects.filter(name=request.user).order_by('-date')  # Use 'name' instead of 'user'
    else:
        cardio_workouts = []
        lifting_workouts = []
        nutrition_plans = []
    
    return render(request, 'pages/home.html', {
        'cardio_workouts': cardio_workouts,
        'lifting_workouts': lifting_workouts,
        'nutrition_plans': nutrition_plans,
    })
def user_is_creator(model_class, object_id_field, user_field_name="user"):
    """
    Decorator to check if the logged-in user is the creator of the object.
    - model_class: The model of the object.
    - object_id_field: The field in the URL that holds the object ID.
    - user_field_name: The name of the field in the model that stores the creator (e.g., 'user').
    """

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):

            object_id = kwargs.get(object_id_field)

            obj = get_object_or_404(model_class, pk=object_id)

            if getattr(obj, user_field_name) != request.user:
                raise Http404("You do not have permission to access this object.")

            return view_func(request, *args, **kwargs)

        return _wrapped_view

    return decorator


class NewLiftView(LoginRequiredMixin, FormView):
    model = LiftingWorkout
    form_class = AddLift
    template_name = "workouts/add_lift.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.name = self.request.user
        form.save()
        return super().form_valid(form)


@login_required
@user_is_creator(LiftingWorkout, "pk", "name")
def edit_lift_view(request, pk):
    workout = get_object_or_404(LiftingWorkout, pk=pk)

    if request.method == "POST":
        form = EditLift(request.POST, instance=workout)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = EditLift(instance=workout)

    return render(
        request, "workouts/edit_lift.html", {"form": form, "workout": workout}
    )


class NewCardioView(LoginRequiredMixin, FormView):
    model = CardioWorkout
    form_class = AddCardio
    template_name = "workouts/add_cardio.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.name = self.request.user
        form.save()
        return super().form_valid(form)


@login_required
@user_is_creator(CardioWorkout, "pk", "name")
def edit_cardio_view(request, pk):
    workout = get_object_or_404(CardioWorkout, pk=pk)

    if request.method == "POST":
        form = EditCardio(request.POST, instance=workout)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = EditCardio(instance=workout)

    return render(
        request, "workouts/edit_cardio.html", {"form": form, "workout": workout}
    )


def search_target_view(request):
    if request.method == "GET":
        form = TargetSearch(request.GET)
        if form.is_valid():
            query = form.cleaned_data["search_choice"]

            url = f"https://exercisedb.p.rapidapi.com/exercises/target/{query}"

            querystring = {"limit": "10", "offset": "0"}

            headers = {
                "x-rapidapi-key": os.getenv("RAPIDAPI_KEY"),
                "x-rapidapi-host": os.getenv("RAPIDAPI_HOST_WORKOUTS"),
            }

            response = requests.get(url, headers=headers, params=querystring)
            data = response.json()

            return render(request, "searches/results.html", {"data": data})

    else:
        form = TargetSearch()

    return render(request, "searches/search.html", {"form": form})


def search_body_part_view(request):
    if request.method == "GET":
        form = BodyPartSearch(request.GET)
        if form.is_valid():
            query = form.cleaned_data["search_choice"]

            url = f"https://exercisedb.p.rapidapi.com/exercises/bodyPart/{query}"

            querystring = {"limit": "10", "offset": "0"}

            headers = {
                "x-rapidapi-key": os.getenv("RAPIDAPI_KEY"),
                "x-rapidapi-host": os.getenv("RAPIDAPI_HOST_WORKOUTS"),
            }

            response = requests.get(url, headers=headers, params=querystring)
            data = response.json()

            return render(request, "searches/results.html", {"data": data})

    else:
        form = BodyPartSearch()

    return render(request, "searches/search.html", {"form": form})


def search_equipment_view(request):
    if request.method == "GET":
        form = EquipmentSearch(request.GET)
        if form.is_valid():
            query = form.cleaned_data["search_choice"]

            url = f"https://exercisedb.p.rapidapi.com/exercises/equipment/{query}"

            querystring = {"limit": "10", "offset": "0"}

            headers = {
                "x-rapidapi-key": os.getenv("RAPIDAPI_KEY"),
                "x-rapidapi-host": os.getenv("RAPIDAPI_HOST_WORKOUTS"),
            }

            response = requests.get(url, headers=headers, params=querystring)
            data = response.json()

            return render(request, "searches/results.html", {"data": data})

    else:
        form = EquipmentSearch()

    return render(request, "searches/search.html", {"form": form})

class CardioWorkoutListView(ListView):
    model = CardioWorkout
    template_name = "workouts/show_cardio.html"
    context_object_name = "cardio_workouts"
    paginate_by = 10  # Optional: for pagination

    def get_queryset(self):
        return CardioWorkout.objects.filter(name=self.request.user).order_by('-date')
    
class LiftingWorkoutListView(ListView):
    model = LiftingWorkout
    template_name = "workouts/lifting_workout_list.html"
    context_object_name = "lifting_workouts"
    paginate_by = 10  # Optional: for pagination

    def get_queryset(self):
        return LiftingWorkout.objects.filter(name=self.request.user).order_by('-date')
    


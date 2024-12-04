from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import LiftingWorkout, CardioWorkout
from .forms import AddLift, EditLift, AddCardio, EditCardio
from django.views.generic import CreateView, FormView, TemplateView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import Http404
from functools import wraps


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

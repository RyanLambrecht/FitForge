from django.urls import path
from .views import NewCardioView, NewLiftView, edit_cardio_view, edit_lift_view

urlpatterns = [
    path("lift/new/", NewLiftView.as_view(), name="add_lift"),
    path("cardio/new/", NewCardioView.as_view(), name="add_cardio"),
    path("lift/edit/<int:pk>/", edit_lift_view, name="edit_lift"),
    path("cardio/edit/<int:pk>/", edit_cardio_view, name="edit_cardio"),
]

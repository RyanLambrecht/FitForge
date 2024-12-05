from django.urls import path
from .views import NewCardioView, NewLiftView, edit_cardio_view, edit_lift_view, search_target_view, search_body_part_view, search_equipment_view

urlpatterns = [
    path("lift/new/", NewLiftView.as_view(), name="add_lift"),
    path("cardio/new/", NewCardioView.as_view(), name="add_cardio"),
    path("lift/edit/<int:pk>/", edit_lift_view, name="edit_lift"),
    path("cardio/edit/<int:pk>/", edit_cardio_view, name="edit_cardio"),
    path("search/targets/", search_target_view, name="search_target"),
    path("search/body_part/", search_body_part_view, name="search_body_part"),
    path("search/equipment/", search_equipment_view, name="search_equipment")
]

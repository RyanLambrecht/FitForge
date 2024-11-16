from django.urls import path
from . import views
from .views import (
    signup_view,
    daily_checkin_view,
    progress_report_view,
    edit_account_view,
)

urlpatterns = [
    path("signup/", signup_view, name="signup"),
    path("edit/<int:pk>/", edit_account_view, name="edit_account"),
    path("daily-checkin/", daily_checkin_view, name="daily_checkin"),
    path("progress-report/", progress_report_view, name="progress_report"),
]

from django.urls import path
from . import views
from .views import daily_checkin_view, progress_report_view

urlpatterns = [
    path("signup/", views.signup_view, name="signup"),
    path("daily-checkin/", daily_checkin_view, name="daily_checkin"),
    path("progress-report/", progress_report_view, name="progress_report"),
]

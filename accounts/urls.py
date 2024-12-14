from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    signup_view,
    daily_checkin_view,
    progress_report_view,
    edit_account_view,
    logout_view,
)

urlpatterns = [
    path("signup/", signup_view, name="signup"),
    path("edit/<int:pk>/", edit_account_view, name="edit_account"),
    path("daily-checkin/", daily_checkin_view, name="daily_checkin"),
    path("progress-report/", progress_report_view, name="progress_report"),
    path('logout/', logout_view, name='logout'),
    path('edit/password/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
]

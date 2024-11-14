from django.urls import path
from . import views
from .views import daily_checkin_view, progress_report_view

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('daily-checkin/', daily_checkin_view, name='daily_checkin'),
    path('progress-report/', progress_report_view, name='progress_report'),
    
]


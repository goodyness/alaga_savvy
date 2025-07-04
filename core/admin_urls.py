from django.urls import path
from . import admin_views

urlpatterns = [
    path('dashboard/', admin_views.dashboard, name='admin_dashboard'),
    path('recent-work/add/', admin_views.add_recent_work, name='add_recent_work'),
]

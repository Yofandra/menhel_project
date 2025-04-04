from django.urls import path
from app.views import view_dashboard as views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
]
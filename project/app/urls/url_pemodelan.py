from django.urls import path
from app.views import view_pemodelan as views

urlpatterns = [
    path('pemodelan/', views.pemodelan, name='pemodelan'),
]
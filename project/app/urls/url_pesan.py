from django.urls import path
from app.views import view_pesan as views

urlpatterns = [
    path('pesan', views.pesan, name='pesan'),
]
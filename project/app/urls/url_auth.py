from django.urls import path
from app.views import view_auth as views

urlpatterns = [
    path('', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
]
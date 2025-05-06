from django.urls import path
from app.views import view_pesan as views

urlpatterns = [
    path('pesan', views.pesan, name='pesan'),
    path('chat/', views.chat_with_rasa, name='chat_with_rasa'),
    path("api/chat-logs/", views.get_chat_logs, name="get_chat_logs"),
]
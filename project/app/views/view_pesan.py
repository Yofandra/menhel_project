from app.models import ChatLogs, User
from django.db import models
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
import requests
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime
from django.views import View

def pesan(request):
    return render(request, 'pesan/index.html')

@csrf_exempt
def chat_with_rasa(request):
    if request.method == "POST":
        data = json.loads(request.body)
        message = data.get("message")

        chat_logs = ChatLogs.objects.create(
            user=request.user,
            message=message,
            tanggal=datetime.now()
        )
        
        rasa_url = "http://localhost:5005/webhooks/rest/webhook"
        payload = {"sender": "user", "message": message}
        response = requests.post(rasa_url, json=payload)
        
        if response.status_code == 200:
            rasa_response = response.json()
            reply = rasa_response[0].get("text") if rasa_response else "Maaf, tidak ada balasan."
            chat_logs.response = reply
            chat_logs.save()
            return JsonResponse({"reply": reply})
        else:
            return JsonResponse({"error": "Gagal menghubungi Rasa"}, status=500)
    return JsonResponse({"error": "Invalid method"}, status=405)

def get_chat_logs(request):
    logs = ChatLogs.objects.filter(user=request.user).order_by('tanggal')
    data = [{
        "message": log.message,
        "response": log.response,
        "datetime": log.tanggal.strftime('%I:%M %p')  # contoh: 10:30 AM
    } for log in logs]
    return JsonResponse({"chat_logs": data})
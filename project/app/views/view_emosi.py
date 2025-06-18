from django.shortcuts import render
from app.models import ChatLogs, ChatSession, User
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from ..predictor import classify_emotion
import json
from django.views import View

def emosi(request):  # Pastikan ini sama dengan yang di url_emosi.py
    sessions = ChatSession.objects.filter(user=request.user)
    selected_session_id = request.GET.get('session')  # ambil session ID dari form GET

    context = {
        'sessions': sessions,
        'selected_session_id': selected_session_id,
    }
    if request.method == 'POST':
        input_text = request.POST.get('teks')
        hasil = classify_emotion(input_text)
        return render(request, 'emosi/index.html', {'hasil': hasil, 'input': input_text})
    
    # Ini untuk kasus GET (pertama kali buka halaman)
    return render(request, 'emosi/index.html', context)

def chat_list(request):
    draw = request.GET.get('draw')
    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 10))
    selected_session_id = request.GET.get('session')  # ambil dari dropdown

    if selected_session_id:
        chatlogs = ChatLogs.objects.filter(session__user=request.user, session__id=selected_session_id)
    else:
        chatlogs = ChatLogs.objects.filter(session__user=request.user)

    total = ChatLogs.objects.filter(session__user=request.user).count()
    filtered = chatlogs.count()
    paginator = Paginator(chatlogs, length)
    chatlogs_page = paginator.get_page(start // length + 1)

    data = []
    for chatlog in chatlogs_page.object_list:
        data.append({
            'id': chatlog.id,
            'message': chatlog.message,
            'emosi': classify_emotion(chatlog.message),
        })

    response_data = {
        'draw': draw,
        'recordsTotal': total,
        'recordsFiltered': filtered,
        'data': data,
    }

    return JsonResponse(response_data)

from django.shortcuts import render

def ringkasan(request):
    return render(request, 'ringkasan/index.html')
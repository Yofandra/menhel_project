from django.shortcuts import render

def pesan(request):
    return render(request, 'pesan/index.html')
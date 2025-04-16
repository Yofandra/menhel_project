from django.shortcuts import render

def emosi(request):
    return render(request, 'emosi/index.html')
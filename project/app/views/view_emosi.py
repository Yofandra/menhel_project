from django.shortcuts import render
from ..predictor import classify_emotion

def emosi(request):  # Pastikan ini sama dengan yang di url_emosi.py
    if request.method == 'POST':
        input_text = request.POST.get('teks')
        hasil = classify_emotion(input_text)
        return render(request, 'emosi/index.html', {'hasil': hasil, 'input': input_text})
    
    # Ini untuk kasus GET (pertama kali buka halaman)
    return render(request, 'emosi/index.html')
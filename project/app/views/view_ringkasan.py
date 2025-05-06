import nltk
nltk.data.path.append("D:/KULIAH/SKRIPSI BISMILLAH/APLIKASI/menhel_project/project/nltk_data")

from django.shortcuts import render
from utils.preprocessing import casefolding, tokenization, remove_punctuation, stopword_removal, stemming
from utils.textrank import textrank_summary
from nltk.tokenize import sent_tokenize
from django.shortcuts import render

# def ringkasan(request):
#     return render(request, 'ringkasan/index.html')

def ringkasan(request):
    # Data dummy
    text = (
        "Akhir -akhir ini, saya merasa benar -benar terputus dari kenyataan. Saya sering merasa sulit untuk membedakan antara apa yang nyata dan apa yang tidak. Misalnya, minggu lalu, saya makan malam dengan keluarga saya, dan tiba -tiba saya mengira saudara lelaki saya akan menyerang saya. Saya tahu itu tidak masuk akal, tetapi rasanya nyata pada saat itu. Ini telah terjadi beberapa kali, tetapi tidak sepanjang waktu. Saya juga mengalami kesulitan berkonsentrasi dan mengingat hal -hal yang telah terjadi baru -baru ini. Saya memiliki beberapa episode depresi di masa lalu, tetapi ini tampaknya sedikit berbeda dengan saya. Bisakah Anda membantu saya mengetahui apa yang terjadi?"
    )
    
    # Gunakan kalimat asli sebelum diproses
    sentences = sent_tokenize(text)

    # Proses untuk tampilan
    original = text
    cleaned = casefolding(text)
    tokens = tokenization(cleaned)
    tokens = remove_punctuation(tokens)
    tokens = stopword_removal(tokens)
    stemmed = stemming(tokens)
    result = ' '.join(stemmed)

    # Ringkasan pakai kalimat asli
    summary = textrank_summary(sentences)

    return render(request, 'ringkasan/index.html', {
        'original': original,
        'processed': result,
        'summary': summary,
    })
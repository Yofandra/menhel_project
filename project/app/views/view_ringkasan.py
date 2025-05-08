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
    text = (
        "Akhir -akhir ini, saya merasa benar -benar terputus dari kenyataan. "
        "Saya sering merasa sulit untuk membedakan antara apa yang nyata dan apa yang tidak. "
        "Misalnya, minggu lalu, saya makan malam dengan keluarga saya, dan tiba -tiba saya mengira saudara lelaki saya akan menyerang saya. "
        "Saya tahu itu tidak masuk akal, tetapi rasanya nyata pada saat itu. "
        "Ini telah terjadi beberapa kali, tetapi tidak sepanjang waktu. "
        "Saya juga mengalami kesulitan berkonsentrasi dan mengingat hal -hal yang telah terjadi baru -baru ini. "
        "Saya memiliki beberapa episode depresi di masa lalu, tetapi ini tampaknya sedikit berbeda dengan saya. "
        "Bisakah Anda membantu saya mengetahui apa yang terjadi?"
    )

    # Kalimat asli
    original_sentences = sent_tokenize(text)

    # Preprocessing tiap kalimat
    preprocessed_sentences = []
    for sentence in original_sentences:
        s = casefolding(sentence)
        s = tokenization(s)
        s = remove_punctuation(s)
        s = stopword_removal(s)
        s = stemming(s)
        s = ' '.join(s)
        preprocessed_sentences.append(s)

    # Summary menggunakan hasil preprocessing
    summary = textrank_summary(preprocessed_sentences, original_sentences)

    return render(request, 'ringkasan/index.html', {
        'original': text,
        'processed': preprocessed_sentences,
        'summary': summary['summary'],
        'tfidf_matrix': summary['tfidf_matrix'],
        'feature_names': summary['feature_names'],
        'cosine_similarity': summary['cosine_similarity'],
        'graph_edges': summary['graph_edges'],
        'pagerank_scores': summary['pagerank_scores'],
    })


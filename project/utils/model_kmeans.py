import re
import csv
import os
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# Load stopwords sekali saja saat import
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_stopwords():
    # Load default stopwords dari Sastrawi
    factory_stopwords = StopWordRemoverFactory()
    stopwords = factory_stopwords.get_stop_words()

    # Load custom stopwords dari CSV
    custom_stopword_path = os.path.join(BASE_DIR, 'utils/data/stopwordbahasa.csv')
    if os.path.exists(custom_stopword_path):
        with open(custom_stopword_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            custom_stopwords = [row[0].strip() for row in reader if row]
            stopwords += custom_stopwords

    return set(stopwords)

# Inisialisasi global (agar tidak reload terus)
STOPWORDS = load_stopwords()
STEMMER = StemmerFactory().create_stemmer()

# Fungsi bersih-bersih text
def clean_text(text):
    if not isinstance(text, str):
        return ''
    text = text.lower()

    # Hilangkan duplikasi huruf berlebih (contoh: "baguuuuus" -> "bagus")
    text = re.sub(r'(.)\1{2,}', r'\1', text)

    # Hapus semua karakter selain huruf dan spasi
    text = re.sub(r'[^a-z\s]', '', text)

    words = text.split()

    # Hapus stopword, stemming, buang kata pendek (<3 huruf)
    words = [STEMMER.stem(word) for word in words if word not in STOPWORDS and len(word) > 2]

    return ' '.join(words)

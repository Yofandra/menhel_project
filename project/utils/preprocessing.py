from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# Fungsi preprocessing
def casefolding(text):
    return text.lower()

def tokenization(text):
    tokenizer = TfidfVectorizer().build_tokenizer()
    return tokenizer(text)

def remove_punctuation(words):
    return [word for word in words if word.isalnum()]

def stopword_removal(words, language='indonesian'):
    stop_words = set(stopwords.words(language))
    return [word for word in words if word not in stop_words]

# Fungsi Stemming
def stemming(words):
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    return [stemmer.stem(word) for word in words]
import numpy as np
import networkx as nx
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def textrank_summary(sentences, top_n=3):
    # TF-IDF
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(sentences)

    # Cosine similarity
    cosine_sim = cosine_similarity(tfidf_matrix)

    # Graph representation
    graph = nx.from_numpy_array(cosine_sim)
    scores = nx.pagerank(graph)

    # Ambil kalimat top berdasarkan score
    ranked = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)
    selected_sentences = [s for _, s in ranked[:top_n]]

    return ' '.join(selected_sentences)

import numpy as np
import networkx as nx
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def textrank_summary(processed_sentences, original_sentences, top_n=3):
    # TF-IDF
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(processed_sentences)
    tfidf_array = tfidf_matrix.toarray()
    feature_names = vectorizer.get_feature_names_out()

    # Cosine similarity
    cosine_sim = cosine_similarity(tfidf_matrix)

    # Graph representation
    graph = nx.from_numpy_array(cosine_sim)
    edges = list(graph.edges(data=True))

    # PageRank
    scores = nx.pagerank(graph)

    # Ringkasan: ambil top-N kalimat berdasarkan PageRank
    ranked = sorted(((scores[i], original_sentences[i]) for i in range(len(original_sentences))), reverse=True)
    selected_sentences = [s for _, s in ranked[:top_n]]
    summary = ' '.join(selected_sentences)

    return {
        'tfidf_matrix': tfidf_array,
        'feature_names': feature_names,
        'cosine_similarity': cosine_sim,
        'graph_edges': edges,
        'pagerank_scores': scores,
        'summary': summary
    }

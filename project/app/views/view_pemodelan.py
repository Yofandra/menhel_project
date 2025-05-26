from django.shortcuts import render
import joblib
from utils.model_kmeans import clean_text  # pastikan fungsi preprocessing dipisah di utils
import os
from django.conf import settings


# Load model & vectorizer
vectorizer = joblib.load(settings.MODEL_DIR / 'vectorizer.pkl')
scaler = joblib.load(settings.MODEL_DIR / 'scaler.pkl')
svd_model = joblib.load(settings.MODEL_DIR / 'svd_model.pkl')
kmeans_model = joblib.load(settings.MODEL_DIR / 'kmeans_model.pkl')
cluster_labels = joblib.load(settings.MODEL_DIR / 'cluster_labels.pkl')

# Fungsi prediksi cluster
def predict_cluster(text_input):
    cleaned = clean_text(text_input)

    # Vectorize
    text_vec = vectorizer.transform([cleaned])

    # Scaling
    text_scaled = scaler.transform(text_vec)

    # Dimensionality Reduction
    text_reduced = svd_model.transform(text_scaled)

    # Predict Cluster
    cluster_number = kmeans_model.predict(text_reduced)[0]

    # Get Cluster Label Name
    cluster_label = cluster_labels.get(cluster_number, "Unknown Cluster")

    return cluster_label

# Views Django (hanya prediksi & tampilkan hasil)
def pemodelan(request):
    prediction_result = None

    if request.method == 'POST':
        user_input = request.POST.get('text_input')
        if user_input:
            prediction_result = predict_cluster(user_input)

    context = {
        'prediction': prediction_result
    }

    return render(request, 'pemodelan/index.html', context)

import nltk

# Tentukan folder tempat menyimpan data
nltk.data.path.append('D:/KULIAH/SKRIPSI BISMILLAH/APLIKASI/menhel_project/project/nltk_data')

# Download resource 'punkt', 'wordnet', dan 'omw-1.4' ke folder yang sudah ditentukan
nltk.download('punkt', download_dir='D:/KULIAH/SKRIPSI BISMILLAH/APLIKASI/menhel_project/project/nltk_data')
nltk.download('wordnet', download_dir='D:/KULIAH/SKRIPSI BISMILLAH/APLIKASI/menhel_project/project/nltk_data')
nltk.download('omw-1.4', download_dir='D:/KULIAH/SKRIPSI BISMILLAH/APLIKASI/menhel_project/project/nltk_data')
nltk.download('punkt_tab', download_dir='D:/KULIAH/SKRIPSI BISMILLAH/APLIKASI/menhel_project/project/nltk_data')
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load data
def load_data():
    with open("data/info.txt", encoding="utf-8") as f:
        lines = f.readlines()
    return [line.strip() for line in lines if line.strip()]

documents = load_data()

# Create TF-IDF vectors
vectorizer = TfidfVectorizer()
doc_vectors = vectorizer.fit_transform(documents)


def search(query, k=3):
    query_vec = vectorizer.transform([query])
    similarities = cosine_similarity(query_vec, doc_vectors)[0]

    top_indices = similarities.argsort()[-k:][::-1]

    return [documents[i] for i in top_indices]
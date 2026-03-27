from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load data
def load_data():
    with open("backend/data/info.txt") as f:
        return f.readlines()

documents = load_data()

# Convert to embeddings
embeddings = model.encode(documents)

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))


def search(query):
    query_vec = model.encode([query])
    distances, indices = index.search(np.array(query_vec), k=2)
    results = [documents[i] for i in indices[0]]
    return " ".join(results)
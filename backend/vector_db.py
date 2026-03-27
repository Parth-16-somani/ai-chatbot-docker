from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

# 🔥 Load and clean data
def load_data():
    with open("data/info.txt", encoding="utf-8") as f:
        lines = f.readlines()

    # 🔥 each line = one chunk
    docs = [line.strip() for line in lines if line.strip()]
    return docs


documents = load_data()

# 🔥 Safety check
if len(documents) == 0:
    raise ValueError("DATA FILE IS EMPTY — FIX info.txt")

# 🔥 Build embeddings
embeddings = model.encode(documents)

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))


def search(query, k=3):

    query_vec = model.encode([query])
    distances, indices = index.search(np.array(query_vec), k)

    results = []
    for i in indices[0]:
        if i < len(documents):
            results.append(documents[i])

    return results   # 🔥 RETURN LIST (NOT STRING)
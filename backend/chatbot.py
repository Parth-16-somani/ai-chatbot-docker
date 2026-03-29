from transformers import pipeline
from vector_db import search

# Stable model (no tokenizer issues)
generator = pipeline("text-generation", model="distilgpt2")

def normalize_query(query):
    return query.lower().replace("explain", "what is").replace("define", "what is")

def get_answer(query):

    results = search(query)

    if not results:
        return "No relevant information found."

    query = normalize_query(query)

    # 🔥 choose best matching sentence
    best = results[0]

    for sentence in results:
        if any(word in sentence.lower() for word in query_words):
            best = sentence
            break

    return best
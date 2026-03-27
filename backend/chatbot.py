from transformers import pipeline
from vector_db import search

generator = pipeline("text-generation", model="gpt2")


def get_answer(query):

    context = search(query)

    prompt = f"""
You are an AI assistant. Answer the question based on the context below.

Context:
{context}

Question: {query}

Answer:
"""

    result = generator(
        prompt,
        max_length=150,
        temperature=0.3
    )

    text = result[0]["generated_text"]

    if "Answer:" in text:
        return text.split("Answer:")[-1].strip()

    return text
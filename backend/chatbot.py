from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")


def get_answer(q: str):
    result = generator(q, max_length=50)
    return result[0]["generated_text"]
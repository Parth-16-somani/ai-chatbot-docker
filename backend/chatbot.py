from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")


def load_data():
    with open("data/info.txt") as f:
        return f.read()


DATA = load_data()


def get_answer(q: str):

    prompt = f"""
You are an AI assistant.
Use the information below to answer the question.

Information:
{DATA}

Question: {q}

Answer:
"""

    result = generator(
        prompt,
        max_length=150,
        num_return_sequences=1,
        temperature=0.3,
    )

    text = result[0]["generated_text"]

    # return only part after Answer:
    if "Answer:" in text:
        return text.split("Answer:")[-1].strip()

    return text
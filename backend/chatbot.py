from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")


def load_data():
    with open("backend/data/info.txt") as f:
        return f.read()


DATA = load_data()


def get_answer(q: str):
    prompt = DATA + "\nQuestion: " + q
    result = generator(prompt, max_length=100)
    return result[0]["generated_text"]
from vector_db import search

# 🔹 Normalize query for better matching
def normalize_query(query):
    query = query.lower()
    query = query.replace("explain", "what is")
    query = query.replace("define", "what is")
    return query


def get_answer(query):

    # 🔹 Normalize input
    query = normalize_query(query)

    # 🔹 Retrieve relevant results (list)
    results = search(query)

    if not results:
        return "No relevant information found."

    # 🔹 Convert query into keyword set
    query_words = set(query.split())

    # 🔹 Score each sentence based on keyword overlap
    best = results[0]
    max_score = 0

    for sentence in results:
        words = set(sentence.lower().split())
        score = len(query_words & words)

        if score > max_score:
            max_score = score
            best = sentence

    return best.strip()
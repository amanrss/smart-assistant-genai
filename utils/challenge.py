from utils.gemini_client import ask_gemini

def generate_challenges(text):

    prompt = f"""
    Generate exactly 3 challenging questions.

    Return only:

    1. Question
    2. Question
    3. Question

    Document:
    {text[:50000]}
    """

    response = ask_gemini(prompt)

    questions = []

    for line in response.split("\n"):
        line = line.strip()

        if line.startswith(("1.", "2.", "3.", "-", "*")):
            q = line.split(".", 1)[-1].strip()
            questions.append(q)

    return questions[:3]


def evaluate_answer(question, answer, document):

    prompt = f"""
    Document:
    {document}

    Question:
    {question}

    User Answer:
    {answer}

    Evaluate the answer.

    Return:
    Score /10
    Correct Answer
    Explanation
    """

    return ask_gemini(prompt)

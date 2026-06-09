from utils.gemini_client import ask_gemini

def generate_challenges(text):

    prompt = f"""
    Generate 5 challenging questions from the document.

    Return only numbered questions.

    Document:
    {text}
    """

    return ask_gemini(prompt)


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

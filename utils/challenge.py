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


def evaluate_answer(document, question, answer):

    prompt = f"""
    Document:
    {document[:50000]}

    Question:
    {question}

    User Answer:
    {answer}

    Evaluate the answer.

    Return:

    SCORE:
    <score out of 10>

    FEEDBACK:
    <feedback>
    """

    response = ask_gemini(prompt)

    try:
        score = response.split("FEEDBACK:")[0].replace("SCORE:", "").strip()
        feedback = response.split("FEEDBACK:")[1].strip()
    except:
        score = "N/A"
        feedback = response

    return score, feedback

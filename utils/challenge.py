from utils.gemini_client import ask_gemini

def generate_questions(text):

    prompt = f"""
    Generate 5 challenging questions from the document.

    Return only numbered questions.

    Document:
    {text}
    """

    return ask_gemini(prompt)

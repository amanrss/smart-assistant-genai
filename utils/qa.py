from utils.gemini_client import ask_gemini

def answer_question(document_text, question):

    prompt = f"""
    Document:
    {document_text}

    Question:
    {question}

    Answer only using information from the document.
    """

    return ask_gemini(prompt)

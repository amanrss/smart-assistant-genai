from utils.gemini_client import ask_gemini

def generate_summary(text):

    prompt = f"""
    Summarize the following document professionally.

    Include:
    1. Overview
    2. Key Points
    3. Important Findings
    4. Conclusion

    Document:
    {text}
    """

    return ask_gemini(prompt)

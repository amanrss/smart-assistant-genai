from utils.gemini_client import ask_gemini

def generate_summary(text, polish=False):

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

    summary = ask_gemini(prompt)

    if polish:
        polish_prompt = f"""
        Improve the following summary by making it more professional,
        concise and grammatically correct.

        Summary:
        {summary}
        """

        summary = ask_gemini(polish_prompt)

    return summary

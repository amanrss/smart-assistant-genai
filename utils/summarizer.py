from utils.gemini_client import ask_gemini

def generate_summary(text, polish=False):

    prompt = f"""
    Summarize the following document professionally.

    Include:
    - Overview
    - Key Points
    - Important Findings
    - Conclusion

    Document:
    {text[:50000]}
    """

    summary = ask_gemini(prompt)

    if polish:
        summary = ask_gemini(
            f"Improve the grammar and professionalism of:\n\n{summary}"
        )

    return summary

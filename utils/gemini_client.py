import google.generativeai as genai
import streamlit as st

api_key = st.secrets.get("GEMINI_API_KEY")

st.write("API Key Present:", api_key is not None)

if api_key:
    st.write("Key Prefix:", api_key[:10])

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.5-flash")
else:
    model = None

def ask_gemini(prompt):
    try:
        if model is None:
            return "No API key found"

        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Gemini Error: {str(e)}"

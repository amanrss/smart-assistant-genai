import google.generativeai as genai
import streamlit as st

api_key = st.secrets.get("GEMINI_API_KEY")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.5-flash")
else:
    model = None

def ask_gemini(prompt):
    if model is None:
        return "❌ Gemini API Key not found. Please configure GEMINI_API_KEY."

    response = model.generate_content(prompt)
    return response.text

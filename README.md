# 📚 Smart Assistant for Research Summarization

An AI-powered research assistant that helps users quickly understand and interact with research papers, reports, and documents using Google's Gemini API.

## 🚀 Live Demo

**Live Application:** [https://smart-assistant-genai-954.streamlit.app/]

---

## 📖 Overview

Smart Assistant for Research Summarization is a Generative AI application that allows users to upload research papers in PDF or TXT format and interact with them intelligently.

The system automatically generates concise summaries, answers user questions based on document content, and provides a challenge-based learning mode to improve comprehension.

---

## ✨ Features

### 📄 Document Upload

* Supports PDF and TXT files
* Automatic text extraction and processing

### 📘 AI-Powered Summarization

* Generates structured summaries
* Highlights key findings and insights
* Produces professional and readable output

### ❓ Ask Anything

* Ask natural language questions about the uploaded document
* Receive contextual answers generated using Gemini
* Includes answer justification and supporting snippets

### 🧠 Challenge Me

* Automatically generates document-based questions
* Evaluates user responses
* Provides feedback and scoring

### ☁️ Cloud Deployment

* Fully deployed using Streamlit Cloud
* Accessible from anywhere through a web browser

---

## 🏗️ System Architecture

```text
User Uploads PDF/TXT
          │
          ▼
Document Parsing
          │
          ▼
Text Extraction
          │
          ▼
Google Gemini API
     ├── Summarization
     ├── Question Answering
     ├── Question Generation
     └── Answer Evaluation
          │
          ▼
Interactive Streamlit UI
```

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### AI & NLP

* Google Gemini API

### Document Processing

* pdfplumber

### Language

* Python

### Deployment

* Streamlit Community Cloud

---

## 📂 Project Structure

```text
smart-assistant-genai/
│
├── app.py
│
├── utils/
│   ├── gemini_client.py
│   ├── summarizer.py
│   ├── qa.py
│   ├── challenge.py
│   └── parser.py
│
├── requirements.txt
│
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/smart-assistant-genai.git

cd smart-assistant-genai
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Gemini API Key

Create:

```text
.streamlit/secrets.toml
```

Add:

```toml
GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
```

---

## ▶️ Run Locally

```bash
streamlit run app.py
```

---

## 🎯 Use Cases

* Research Paper Analysis
* Academic Study Assistance
* Literature Review Support
* Technical Document Understanding
* Student Learning Enhancement
* Knowledge Extraction from PDFs

---

## 🔮 Future Enhancements

* Retrieval-Augmented Generation (RAG)
* Vector Database Integration
* Multi-Document Comparison
* PDF Annotation Support
* Citation Extraction
* Export Summary as PDF
* Conversational Memory
* Advanced Semantic Search

---

## 👨‍💻 Author

**Aman Singh**

B.Tech (Data Science)

Noida Institute of Engineering and Technology

---

## 📜 License

This project is intended for educational, research, and portfolio purposes.

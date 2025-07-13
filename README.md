# 🔮 Smart Assistant for Research Summarization

An AI-powered assistant that helps researchers, students, and educators quickly understand and interact with academic documents. Built entirely on **free open-source models**, this app extracts summaries, answers deep questions, evaluates answers, and explains its reasoning. Designed with an intuitive Streamlit interface.

---

## 🔁 What It Does

- 📄 **Upload a PDF/TXT research paper**
- 📝 **Auto Summary**: Generates a rich abstract with optional grammar polishing
- ❓ **Ask Anything**: Answer any question from the document using semantic search + context memory
- 🧠 **Challenge Me**: Auto-generated logic questions to test comprehension
- ✅ **Evaluate Answers**: Gives feedback and scoring based on meaning match
- 🧠 **Memory-Enabled**: Handles follow-up questions with retained context
- 🔍 **Answer Highlighting**: Shows exactly which paragraph supports each answer

---

## 🚀 Features Overview

| Feature                        | Description                                                                 |
|------------------------------- |---------------------------------------------------------------------------- |
| 📂 Document Upload            | Upload `.pdf` or `.txt` files                                              |
| 📝 Grammar-Polished Summaries | Toggle to clean and enhance auto summaries                                 |
| 🧠 Ask Anything Mode          | Extracts context-aware answers from anywhere in the doc                    |
| 🔎 Semantic Search Ranking    | Uses sentence transformers to rank relevant chunks                         |
| 📖 Justification & Snippet    | Shows paragraph number and exact source snippet                            |
| 💬 Context Memory             | Supports intelligent follow-up questions                                   |
| 🧠 Challenge Generator        | Generates 3 logic-based questions from the uploaded doc                    |
| ✅ Answer Evaluator           | Compares user input vs doc and gives smart feedback                        |

---

## 🛠️ Tech Stack

- `Python 3.9+`
- `Streamlit`
- `Transformers`
- `Sentence-Transformers`
- `pdfplumber`

---

## 🏠 Local Setup

### 1. Clone the repo
```bash
git clone https://github.com/amanrss/smart-assistant-genai.git
cd smart-assistant-genai
```

### 2. Set up virtual environment (Windows)
```bash
python -m venv venv
venv\Scripts\activate
```
*For Linux/macOS:* `source venv/bin/activate`

### 3. Install requirements
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
streamlit run app.py
```

---
## 📸 Screenshots 

UPLOAD
![Upload](Upload.png)

SUMMARY
![Summary](Summary.png)

Ask Anything
![Ask anything](AskAnything.png)

CHALLENGE ME
![ChallengeMe](ChallengeMe.png)

---

## 📂 Folder Structure

```
smart-assistant-genai/
├── app.py
├── README.md
├── requirements.txt
└── utils/
    ├── parser.py
    ├── summarizer.py
    ├── qa.py
    └── challenge.py
```

---
 👤 Author

**Aman Singh**   
📧 [amanrss954@gmail.com](mailto:amanrss954@gmail.com)

## 🔓 License
MIT License — free to use, modify and share.

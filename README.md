# Gemini Student DB Query

> ✨ An AI-powered application that converts natural language prompts into SQL queries to fetch student database records using **Gemini API** and **Streamlit**.

---

## 🚀 Project Overview

This project demonstrates how to use a **Large Language Model (LLM)** (Gemini) to:
- Understand a **natural language** query from the user
- Generate a corresponding **SQL query**
- Execute it on a **SQLite student database**
- Display the retrieved results interactively using **Streamlit**

---

## 📚 Tech Stack

- **Python 3.10+**
- **SQLite3** — Lightweight database for Student records
- **Google Generative AI (Gemini) API** — Text-to-SQL generation
- **Streamlit** — User interface for querying
- **dotenv** — Secure API key management

---

## 🛠 Features

- Convert plain English queries into SQL
- Fetch student information dynamically
- View results instantly in an intuitive UI
- Secure API usage with environment variables
- Modular codebase with extendable functions

---

## ⚙️ Setup Instructions

1. **Clone the repo**
```bash
git clone https://github.com/your-username/gemini-student-db-query.git
cd gemini-student-db-query
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Create `.env` file**
```env
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

4. **Run the application**
```bash
streamlit run app.py
```

---

## 🧠 Example User Prompts

- "Show all students who scored more than 80 marks"
- "List students from class 10, section A"
- "Retrieve names of students sorted by marks"

---

## 🔒 Important

- Ensure your Gemini API key has **Generative AI access** enabled.
- Do not expose `.env` or API keys publicly.

---

# 🚀 Let's turn plain English into powerful SQL queries!

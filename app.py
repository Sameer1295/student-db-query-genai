import os
import sqlite3
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env file
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# List models available
    
# Configure Gemini Pro
genai.configure(api_key=GEMINI_API_KEY)
models = genai.list_models()

print("Models available under your API key:")
for model in models:
    print(f"- {model.name}")

# Create a model instance
model = genai.GenerativeModel('gemini-2.0-flash')

# Define the base prompt
prompt_base = """
You are an expert SQL developer.
Convert the following user request into a valid SQLite SQL query 
which can be executed directly on a table called STUDENT with columns (NAME, CLASS, SECTION, MARKS).

Only provide the SQL query, no explanations.
"""

# Function 1: Generate SQL query from user prompt
def generate_query_from_prompt(user_text):
    full_prompt = prompt_base + "\nUser Request: " + user_text
    response = model.generate_content(full_prompt)
    sql_query = response.text.strip().strip('```sql').strip('```')
    return sql_query

# Function 2: Fetch data from DB using the SQL query
def fetch_data_from_table(sql_query):
    connection = sqlite3.connect("student.db")
    cursor = connection.cursor()
    try:
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        connection.close()
        return rows
    except Exception as e:
        connection.close()
        return f"Error: {e}"

# --- Streamlit UI ---
st.title("🛠️ Natural Language to SQL Query Generator")

user_input = st.text_input("Enter your request (e.g., Show all students with marks above 80):")

if st.button("Submit"):
    if user_input:
        with st.spinner("Generating SQL query..."):
            sql_query = generate_query_from_prompt(user_input)
            st.code(sql_query, language='sql')

            data = fetch_data_from_table(sql_query)
            
            if isinstance(data, str) and data.startswith("Error"):
                st.error(data)
            else:
                st.success("Query executed successfully!")
                if data:
                    for row in data:
                        st.write(row)
                else:
                    st.info("No data found for the given query.")

import openai
import streamlit as st
st.markdown("### ✅ OpenAI Connection Test")
try:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": "Say hello to my classroom!"}
        ]
    )
    message = response['choices'][0]['message']['content']
    st.success("Connected to GPT-4 ✅\n\nGPT says: " + message)
except Exception as e:
    st.error("❌ OpenAI error: " + str(e))
# app.py
import streamlit as st
import openai
import pandas as pd
import gspread
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials

# --- SETUP ---
openai.api_key = st.secrets["openai"]["api_key"]

# Google Sheets setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(st.secrets["gcp_service_account"], scope)
client = gspread.authorize(creds)
sheet = client.open("Antiracist Lesson Connections").sheet1

# --- UI ---
st.title("🌱 Antiracist Lesson Planner with Community & Cultural Wealth")

with st.form("lesson_form"):
    grade = st.selectbox("🎓 Grade Level", ["TK-2", "3-5", "6-8", "9-12"])
    subject = st.selectbox("📘 Subject", ["Math", "Science", "ELA", "Social Science", "World Language", "Multiple Subjects", "Other"])
    standard = st.text_area("📚 Standard (Paste the full text)")
    zip_code = st.text_input("📍 ZIP Code (for local connections)")
    submit = st.form_submit_button("Generate Antiracist Connections")

# --- PROMPT FUNCTION ---
def generate_connections(standard, grade, subject, zip_code):
    prompt = f"""
You are an antiracist educator designing culturally sustaining instruction. The standard is:
"{standard}"
The user is teaching {subject} at the {grade} level in ZIP code {zip_code}.

Generate:
1. A critical or justice-centered real-world context
2. A project idea that connects to students’ lives or communities
3. A caregiver engagement question
4. A connection to a diverse mathematician, activist, or cultural practice
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a helpful, equity-focused educator assistant."},
                 {"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

# --- GENERATE & DISPLAY ---
if submit and standard:
    with st.spinner("Generating antiracist connections..."):
        output = generate_connections(standard, grade, subject, zip_code)
        st.markdown("### 🧠 Generated Suggestions")
        st.markdown(output)

        # Save to Google Sheet
        row = [datetime.now().isoformat(), grade, subject, standard, zip_code, output]
        sheet.append_row(row)

        st.success("Saved to Google Sheet ✅")

import streamlit as st
import openai
import json
import gspread
from datetime import datetime
from google.oauth2.service_account import Credentials

# --- STREAMLIT PAGE SETUP ---
st.set_page_config(page_title="Antiracist Lesson Planner", layout="centered")
st.title("🌱 Antiracist Lesson Planner with Community & Cultural Wealth")

# --- OPENAI SETUP ---
client = openai.OpenAI(api_key=st.secrets["openai"]["api_key"])

# --- GOOGLE SHEETS SETUP ---
scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
creds_dict = json.loads(st.secrets["gcp_service_account_json"]["json"])
creds = Credentials.from_service_account_info(creds_dict, scopes=scope)
client_gsheets = gspread.authorize(creds)
sheet = client_gsheets.open("Antiracist Lesson Connections").sheet1

# --- FORM UI ---
with st.form("lesson_form"):
    grade = st.selectbox("🎓 Grade Level", ["TK-2", "3-5", "6-8", "9-12"])
    subject = st.selectbox("📘 Subject", ["Math", "Science", "ELA", "Social Science", "World Language", "Multiple Subjects", "Other"])
    standard = st.text_area("📚 Standard (Paste the full text)")
    zip_code = st.text_input("📍 ZIP Code (for local community context)")
    submit = st.form_submit_button("Generate Antiracist Lesson Ideas")

# --- GPT CALL FUNCTION ---
def generate_antiracist_content(standard, grade, subject, zip_code):
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
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful, equity-focused educator assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# --- HANDLE SUBMIT ---
if submit and standard:
    with st.spinner("🧠 Generating antiracist lesson connections..."):
        output = generate_antiracist_content(standard, grade, subject, zip_code)
        st.success("Here are your personalized, justice-centered ideas:")
        st.markdown("### 📘 Lesson Suggestions")
        st.markdown(output)

        # Save to Google Sheet
        timestamp = datetime.now().isoformat()
        row = [timestamp, grade, subject, standard, zip_code, output]
        sheet.append_row(row)
        st.success("✅ Saved to Google Sheet successfully!")

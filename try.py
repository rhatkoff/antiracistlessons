import streamlit as st

# App Title
st.title('🌱 Antiracist & Community Cultural Wealth Lesson Planner')

# Sidebar for lesson details
st.sidebar.header('📋 Lesson Details')
subject = st.sidebar.selectbox(
    'Subject',
    [
        '📐 Math',
        '🔬 Science',
        '📚 English Language Arts',
        '🌍 Social Science',
        '🗣️ World Language',
        '🎒 Multiple Subjects',
        '🧩 Other'
    ]
)
grade = st.sidebar.selectbox('🎓 Grade Level', ['TK-2', '3-5', '6-8', '9-12'])
topic = st.sidebar.text_input('🧠 Lesson Topic', 'Vertebrate Biology')
zip_code = st.sidebar.text_input('📍 ZIP Code', '91711')

# Main content
st.header('📑 Personalized Lesson Plan Suggestions')

st.write(f'**Subject:** {subject}')
st.write(f'**Grade:** {grade}')
st.write(f'**Topic:** {topic}')
st.write(f'**ZIP Code:** {zip_code}')

# Antiracist connections
st.subheader('✊🏽 Antiracist Connections')
st.markdown("""
- **🗣️ Discussion Topic:** How has racism shaped our understanding of this topic historically and currently?
- **📄 Assignment:** Research how communities of color have been impacted by or contributed to this area of study.
- **📝 Assessment:** Students critically analyze a resource/text to identify potential biases.
- **👨🏽‍👩🏽‍👧🏽 Questions for Caregivers:** Discuss family experiences related to the topic and any knowledge passed down through generations.
- **🤝🏽 Community Project:** Organize interviews with community elders about their experiences with this subject.
""")

# Local community connections
st.subheader('🏘️ Local Community Connections')
st.markdown(f"""
Based on your ZIP code ({zip_code}), consider connecting with:
- 🏛️ Local museums or cultural centers relevant to your topic
- 🏡 Community-based organizations that support diverse voices and experiences
- 🎓 Nearby universities or colleges for guest speakers and expertise
- 📍 Historical landmarks or sites related to the topic
""")

# Relevant & Diverse Voices
st.subheader('👩🏽‍🏫 Relevant & Diverse Scholars, Activists, and Experts')
st.markdown("""
- 🎙️ Highlight scholars or activists who have critically engaged with issues of race and equity in your subject area.
- 📚 Identify experts whose lived experiences provide valuable perspectives.
- 🔗 Include resources or writings by these individuals in your teaching materials.
""")

# Standards Section
st.subheader('📘 Standards Alignment')
st.markdown("""
- 🏛️ **California State Standards:** Search for relevant content standards at [CDE Content Standards](https://www.cde.ca.gov/be/st/ss/).
- 🔬 **NGSS (Next Generation Science Standards):** Match disciplinary core ideas, science practices, and crosscutting concepts at [NextGenScience.org](https://www.nextgenscience.org/).
- 🗂️ **CA ELD Standards:** Refer to proficiency level descriptors and Part I/II standards at [CDE ELD Standards](https://www.cde.ca.gov/sp/el/er/eldstandards.asp).

💡 *Pro Tip:* Align your content, language objectives, and social justice goals for deeper impact.
""")

# Generate Downloadable Template
lesson_plan = f"""
Subject: {subject}
Grade: {grade}
Topic: {topic}
ZIP Code: {zip_code}

Antiracist Connections:
- Discussion Topic:
- Assignment:
- Assessment:
- Questions for Caregivers:
- Community Project:

Local Community Connections:
- Local Resources:
- Organizations:
- Experts:

Relevant & Diverse Voices:
- Scholars:
- Activists:
- Experts:

Standards Alignment:
- California State Standards:
- NGSS:
- CA ELD Standards:
"""

st.download_button('📥 Download Lesson Plan Template', lesson_plan, file_name='personalized_lesson_plan.txt')

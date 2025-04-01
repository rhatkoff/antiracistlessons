import streamlit as st

# App Title
st.title('Antiracist & Community Cultural Wealth Lesson Planner')

# Sidebar for lesson details
st.sidebar.header('Lesson Details')
subject = st.sidebar.selectbox('Subject', ['Biology', 'Math', 'English', 'History', 'Other'])
grade = st.sidebar.selectbox('Grade Level', ['K-2', '3-5', '6-8', '9-12'])
topic = st.sidebar.text_input('Lesson Topic', 'Vertebrate Biology')

# Main content
st.header('Lesson Plan Generator')

st.write(f'**Subject:** {subject}')
st.write(f'**Grade:** {grade}')
st.write(f'**Topic:** {topic}')

# Antiracist prompts
st.subheader('🧠 Antiracist Connection')
st.markdown("""
- **Perspective Check:** Whose voices are included or excluded from your topic?
- **Historical Context:** How has this content historically been used to reinforce or resist racism?
- **Critical Inquiry:** What critical questions can students explore to challenge dominant narratives?
""")

# Community Cultural Wealth
st.subheader('🌎 Community & Cultural Wealth Connection')
st.markdown("""
Using Yosso's Model, consider:
- **Aspirational:** How does this lesson connect to students' hopes and dreams?
- **Linguistic:** How can students' home languages or ways of speaking enrich this lesson?
- **Familial:** Can family experiences or traditions connect to this content?
- **Social:** How does this lesson help students leverage community networks and relationships?
- **Navigational:** What life skills does this lesson affirm or develop?
- **Resistance:** How can students recognize or challenge injustice through this content?
""")

# Generate Downloadable Template
lesson_plan = f"""
Subject: {subject}
Grade: {grade}
Topic: {topic}

Antiracist Connections:
- Whose perspectives are included/excluded?
- Historical context:
- Critical questions:

Community Cultural Wealth Connections:
- Aspirational:
- Linguistic:
- Familial:
- Social:
- Navigational:
- Resistance:
"""

st.download_button('📥 Download Lesson Plan Template', lesson_plan, file_name='lesson_plan_template.txt')

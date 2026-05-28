import streamlit as st
import pandas as pd
import random
from google import genai

GOOGLE_API_KEY = st.secrets["GOOGLE_API"]
genai.Client(api_key=GOOGLE_API_KEY)

def ai_chat(user_input):
    try:
        response = model.generate_content(
            model='gemeni-2.5-flash-lite',
            contents=user_input
        )
        return response.text
    except Exception as e:
        return f"Error: {e}"

# 2 then functions
def ai_chat(user_input):
    response = model.generate_content(
        model='gemeni-2.5-flash-lite',
        contents=user_input
    )
    return response.text

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
    page_title="UNIConnect",
    page_icon="🎓",
    layout="wide"
)

# -------------------------
# CUSTOM CSS
# -------------------------
st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
}

.main {
    background: linear-gradient(to bottom right, #0f172a, #111827);
    color: white;
}

.hero {
    text-align: center;
    padding: 25px;
    border-radius: 20px;
    background: linear-gradient(135deg, #1e293b, #0f172a);
    border: 1px solid #334155;
    margin-bottom: 20px;
}

.hero h1 {
    color: #38bdf8;
    font-size: 55px;
    margin-bottom: 5px;
}

.hero p {
    color: #cbd5e1;
    font-size: 18px;
}

.card {
    background: #1e293b;
    padding: 18px;
    border-radius: 16px;
    margin-bottom: 15px;
    border: 1px solid #334155;
    transition: 0.3s;
}

.card:hover {
    transform: scale(1.02);
    border-color: #38bdf8;
}

.match-score {
    color: #38bdf8;
    font-size: 20px;
    font-weight: bold;
}

.stButton>button {
    width: 100%;
    border-radius: 12px;
    height: 50px;
    font-size: 16px;
    font-weight: bold;
    background: linear-gradient(90deg, #0ea5e9, #2563eb);
    color: white;
    border: none;
}

.stTextInput input {
    border-radius: 10px;
}

.sidebar .sidebar-content {
    background-color: #111827;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# DATABASE
# -------------------------
students = pd.DataFrame([

    {"name": "Ali 🎮", "course": "computer science", "interests": ["ai", "gaming", "music"]},
    {"name": "Sara ✈️", "course": "business", "interests": ["marketing", "travel", "music"]},
    {"name": "John 🤖", "course": "engineering", "interests": ["robotics", "ai", "chess"]},
    {"name": "Mia 🎨", "course": "design", "interests": ["art", "uiux", "photography"]},
    {"name": "Raj 🚀", "course": "computer science", "interests": ["coding", "ai", "startups"]},

    {"name": "Noah 🎧", "course": "business", "interests": ["finance", "music", "stocks"]},
    {"name": "Emma 📸", "course": "design", "interests": ["photography", "editing", "art"]},
    {"name": "Liam ⚙️", "course": "engineering", "interests": ["machines", "robotics", "physics"]},
    {"name": "Sophia 📊", "course": "business", "interests": ["marketing", "data", "strategy"]},
    {"name": "Ethan 💻", "course": "computer science", "interests": ["coding", "ai", "web"]},

    {"name": "Arjun 🎮", "course": "computer science", "interests": ["gaming", "coding", "ai"]},
    {"name": "Meera 🎨", "course": "design", "interests": ["uiux", "drawing", "fashion"]},
    {"name": "Daniel 🧠", "course": "engineering", "interests": ["ai", "math", "robotics"]},
    {"name": "Olivia 💼", "course": "business", "interests": ["networking", "finance", "travel"]},

    {"name": "Chris 🎵", "course": "computer science", "interests": ["music", "gaming", "coding"]},
    {"name": "Aisha 📷", "course": "design", "interests": ["art", "photography", "travel"]},
    {"name": "Kevin 🛠️", "course": "engineering", "interests": ["cars", "robotics", "gaming"]},
    {"name": "Zara 🌍", "course": "business", "interests": ["marketing", "travel", "fashion"]},
])

# -------------------------
# MATCHING LOGIC
# -------------------------
def match_students(user_interests, user_course):

    results = []

    for _, row in students.iterrows():

        score = 0

        # same course bonus
        if user_course.lower() == row["course"].lower():
            score += 3

        # common interests
        common = set(user_interests).intersection(set(row["interests"]))
        score += len(common) * 2

        # compatibility label
        if score >= 7:
            level = "🔥 best match"
        elif score >= 5:
            level = "⭐ strong match"
        elif score >= 3:
            level = "👍 good match"
        else:
            level = "🙂 possible friend"

        if score > 0:
            results.append({
                "name": row["name"],
                "course": row["course"],
                "interests": row["interests"],
                "score": score,
                "common": list(common),
                "level": level
            })

    return sorted(results, key=lambda x: x["score"], reverse=True)

# -------------------------
# HERO SECTION
# -------------------------
st.markdown("""
<div class="hero">
    <h1>🎓 UNIConnect</h1>
    <p>find university friends with similar interests and courses</p>
</div>
""", unsafe_allow_html=True)

# -------------------------
# SIDEBAR
# -------------------------
menu = st.sidebar.radio(
    "navigation",
    ["🏠 social match", "🤖 ai assistant", "📊 community stats"]
)

# -------------------------
# DEMO PROFILES
# -------------------------
demo_profiles = {
    "custom input": {"course": "", "interests": ""},
    "ali gamer": {"course": "computer science", "interests": "ai gaming music"},
    "business traveler": {"course": "business", "interests": "marketing travel fashion"},
    "engineer robot": {"course": "engineering", "interests": "robotics ai physics"},
    "designer artist": {"course": "design", "interests": "art photography uiux"},
}

# =========================================================
# PAGE 1 — SOCIAL MATCH
# =========================================================
if menu == "🏠 social match":

    st.subheader("find your people")

    selected = st.selectbox(
        "choose a demo profile",
        list(demo_profiles.keys())
    )

    col1, col2 = st.columns(2)

    with col1:
        course = st.text_input(
            "your course",
            demo_profiles[selected]["course"]
        )

    with col2:
        interests = st.text_input(
            "your interests",
            demo_profiles[selected]["interests"]
        )

    if st.button("find matches 🔍"):

        if course and interests:

            user_interests = interests.lower().split()

            matches = match_students(user_interests, course)

            st.markdown("## matches found")

            if not matches:
                st.warning("no matches found")

            else:
                for match in matches:

                    st.markdown(f"""
                    <div class="card">

                    <h3>{match['name']}</h3>

                    <p><b>course:</b> {match['course']}</p>

                    <p><b>interests:</b> {', '.join(match['interests'])}</p>

                    <p><b>common interests:</b> {', '.join(match['common'])}</p>

                    <p class="match-score">
                    {match['score']} points • {match['level']}
                    </p>

                    </div>
                    """, unsafe_allow_html=True)

        else:
            st.error("please fill in all fields")

# =========================================================
# PAGE 2 — AI ASSISTANT
# =========================================================
elif menu == "🤖 ai assistant":

    st.subheader("talk to the ai assistant")

    user_input = st.text_input("ask something")

    if st.button("send message"):

        if user_input.strip():
            response = ai_chat(user_input)
            st.success(response)
        else:
            st.warning("type something first")

# =========================================================
# PAGE 3 — COMMUNITY STATS
# =========================================================
elif menu == "📊 community stats":

    st.subheader("community overview")

    total_students = len(students)

    cs_students = len(students[students["course"] == "computer science"])
    business_students = len(students[students["course"] == "business"])
    engineering_students = len(students[students["course"] == "engineering"])
    design_students = len(students[students["course"] == "design"])

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("students", total_students)
    col2.metric("computer science", cs_students)
    col3.metric("business", business_students)
    col4.metric("engineering", engineering_students)

    st.markdown("---")

    st.subheader("popular interests")

    all_interests = []

    for interests in students["interests"]:
        all_interests.extend(interests)

    interest_count = pd.Series(all_interests).value_counts()

    st.bar_chart(interest_count)

    st.subheader("student database")

    st.dataframe(students, use_container_width=True)

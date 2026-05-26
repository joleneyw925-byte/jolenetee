import streamlit as st
import pandas as pd

# -------------------------
# page config (makes it look cleaner)
# -------------------------
st.set_page_config(page_title="UNIConnect", page_icon="🎓", layout="centered")

# -------------------------
# demo database
# -------------------------
students = pd.DataFrame([
    {"name": "ali", "course": "computer science", "interests": ["ai", "gaming", "music"]},
    {"name": "sara", "course": "business", "interests": ["marketing", "music", "travel"]},
    {"name": "john", "course": "engineering", "interests": ["robotics", "ai", "chess"]},
    {"name": "mia", "course": "design", "interests": ["art", "uiux", "photography"]},
    {"name": "raj", "course": "computer science", "interests": ["coding", "ai", "startups"]},
])

# -------------------------
# matching logic
# -------------------------
def match_students(user_interests, user_course):
    results = []

    for _, row in students.iterrows():
        score = 0

        if user_course.lower() == row["course"].lower():
            score += 2

        common = set(user_interests).intersection(set(row["interests"]))
        score += len(common)

        if score > 0:
            results.append((row["name"], row["course"], row["interests"], score))

    return sorted(results, key=lambda x: x[3], reverse=True)

# -------------------------
# demo chat
# -------------------------
def ai_chat(user_input):
    user_input = user_input.lower()

    if "friend" in user_input:
        return "try matching with people in same course + shared interests"
    if "ai" in user_input:
        return "ai matching is based on shared interest overlap scoring"
    if "help" in user_input:
        return "select a demo profile or type your own interests"
    return "ask me about friends, courses or matching"

# -------------------------
# ui header (more alive look)
# -------------------------
st.markdown("""
    <div style='text-align:center; padding:10px'>
        <h1>🎓 UNIConnect</h1>
        <p>find friends based on interests + courses</p>
    </div>
""", unsafe_allow_html=True)

menu = st.sidebar.radio("navigation", ["social match", "ai chat"])

# -------------------------
# demo profiles
# -------------------------
demo_profiles = {
    "custom input": {"course": "", "interests": ""},
    "ali cs gamer": {"course": "computer science", "interests": "ai gaming music"},
    "sara business": {"course": "business", "interests": "marketing music travel"},
    "john engineer": {"course": "engineering", "interests": "robotics ai chess"},
    "mia design": {"course": "design", "interests": "art uiux photography"},
    "raj cs startup": {"course": "computer science", "interests": "coding ai startups"},
}

# -------------------------
# page 1 - social match
# -------------------------
if menu == "social match":

    st.subheader("find your people")

    selected = st.selectbox("choose a demo profile", list(demo_profiles.keys()))

    course = st.text_input("your course", demo_profiles[selected]["course"])
    interests = st.text_input("your interests (space separated)", demo_profiles[selected]["interests"])

    if st.button("find matches 🔍"):

        if course and interests:
            user_interests = interests.split()

            matches = match_students(user_interests, course)

            st.markdown("### matches found")

            if not matches:
                st.warning("no matches found try different interests")
            else:
                for name, course, ints, score in matches:
                    st.markdown(f"""
                    ---
                    **name:** {name}  
                    **course:** {course}  
                    **interests:** {', '.join(ints)}  
                    **match score:** {score}
                    """)
        else:
            st.error("fill in all fields")

# -------------------------
# page 2 - ai chat
# -------------------------
if menu == "ai chat":

    st.subheader("ai assistant")

    user_input = st.text_input("ask something")

    if st.button("send"):
        response = ai_chat(user_input)
        st.success(response)

# -------------------------
# PAGE SETUP (AESTHETIC)
# -------------------------
st.set_page_config(page_title="UNIConnect", page_icon="🎓", layout="centered")

st.markdown("""
<style>
    .main {
        background-color: #0f172a;
        color: white;
    }
    h1 {
        text-align: center;
        color: #38bdf8;
    }
    .card {
        background: linear-gradient(135deg, #1e293b, #0f172a);
        padding: 15px;
        border-radius: 12px;
        margin-bottom: 10px;
        border: 1px solid #334155;
    }
</style>
""", unsafe_allow_html=True)

# -------------------------
# BIG DEMO DATABASE (30+ USERS)
# -------------------------
students = pd.DataFrame([
    {"name": "ali 🎮", "course": "computer science", "interests": ["ai", "gaming", "music"]},
    {"name": "sara ✈️", "course": "business", "interests": ["marketing", "travel", "music"]},
    {"name": "john 🤖", "course": "engineering", "interests": ["robotics", "ai", "chess"]},
    {"name": "mia 🎨", "course": "design", "interests": ["art", "uiux", "photography"]},
    {"name": "raj 🚀", "course": "computer science", "interests": ["coding", "ai", "startups"]},

    {"name": "noah 🎧", "course": "business", "interests": ["finance", "music", "stocks"]},
    {"name": "emma 📸", "course": "design", "interests": ["photography", "editing", "art"]},
    {"name": "liam ⚙️", "course": "engineering", "interests": ["machines", "robotics", "physics"]},
    {"name": "sophia 📊", "course": "business", "interests": ["marketing", "data", "strategy"]},
    {"name": "ethan 💻", "course": "computer science", "interests": ["coding", "ai", "web"]},

    {"name": "arjun 🎮", "course": "computer science", "interests": ["gaming", "coding", "ai"]},
    {"name": "meera 🎨", "course": "design", "interests": ["uiux", "drawing", "fashion"]},
    {"name": "daniel 🧠", "course": "engineering", "interests": ["ai", "math", "robotics"]},
    {"name": "olivia ✈️", "course": "business", "interests": ["gaming", "coding", "ai"]},])
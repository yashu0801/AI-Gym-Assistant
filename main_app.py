import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

st.set_page_config(page_title="AI Gym Assistant Pro", layout="wide")

# ---------------- LOGIN SESSION ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---------------- PREMIUM STYLE ----------------
st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
background-image:url('https://images.unsplash.com/photo-1517836357463-d25dfeac3438');
background-size:cover;
background-position:center;
background-attachment:fixed;
}

.main{
background:rgba(0,0,0,0.72);
padding:20px;
border-radius:20px;
}

.hero{
text-align:center;
font-size:60px;
font-weight:bold;
color:#38bdf8;
text-shadow:0px 0px 20px #38bdf8;
}

.sub{
text-align:center;
font-size:22px;
color:white;
margin-bottom:30px;
}

.stMetric{
background:rgba(15,23,42,0.85);
padding:15px;
border-radius:20px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- LOGIN PAGE ----------------
if not st.session_state.logged_in:

    st.markdown(
        "<div class='hero'>🏋️ AI Gym Assistant Pro</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='sub'>AI Powered Fitness Platform</div>",
        unsafe_allow_html=True
    )

    st.image(
        [
            "https://images.unsplash.com/photo-1518611012118-696072aa579a",
            "https://images.unsplash.com/photo-1517838277536-f5f99be501cd",
            "https://images.unsplash.com/photo-1517963879433-6ad2b056d712"
        ],
        width=250
    )

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if username == "admin" and password == "admin123":

            st.session_state.logged_in = True
            st.rerun()

        else:
            st.error("Invalid credentials")

    st.stop()

# ---------------- SIDEBAR ----------------
with st.sidebar:

    selected = option_menu(
        "AI Gym Assistant",
        [
            "Dashboard",
            "BMI Calculator",
            "Walking Tracker",
            "Workout Reminder",
            "AI Chatbot",
            "Food Upload",
            "PDF Upload",
            "Analytics"
        ],
        icons=[
            "house",
            "heart",
            "activity",
            "bell",
            "robot",
            "image",
            "file-earmark-pdf",
            "bar-chart"
        ],
        default_index=0
    )

# ---------------- TITLE ----------------
st.markdown(
    "<div class='hero'>🏋️ AI Gym Assistant Pro</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub'>Transform Your Fitness Journey With AI</div>",
    unsafe_allow_html=True
)

# ---------------- DASHBOARD ----------------
if selected == "Dashboard":

    st.subheader("🔥 Premium Fitness Dashboard")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Calories", "540 kcal", "+12%")
    c2.metric("Steps", "8,240", "+10%")
    c3.metric("Workout Streak", "9 Days", "+2")
    c4.metric("Water Intake", "3.2 L", "+0.4")

    st.progress(80)

    st.success("Consistency creates transformation.")

# ---------------- BMI ----------------
elif selected == "BMI Calculator":

    st.subheader("📏 BMI Calculator")

    h = st.number_input("Height (cm)", 100)
    w = st.number_input("Weight (kg)", 20)

    if st.button("Calculate BMI"):

        bmi = w / ((h / 100) ** 2)

        st.success(f"Your BMI: {bmi:.2f}")

        if bmi < 18.5:
            st.warning("Underweight")

        elif bmi < 25:
            st.success("Healthy")

        else:
            st.error("Overweight")

# ---------------- WALKING TRACKER ----------------
elif selected == "Walking Tracker":

    st.subheader("🚶 Smart Walking Tracker")

    steps = st.number_input("Enter Steps", 0)

    distance = (steps * 0.762) / 1000
    calories = steps * 0.04

    c1, c2, c3 = st.columns(3)

    c1.metric("Steps", steps)
    c2.metric("Distance", f"{distance:.2f} km")
    c3.metric("Calories", f"{calories:.0f} kcal")

    goal = min(steps / 10000, 1.0)

    st.progress(goal)

# ---------------- WORKOUT REMINDER ----------------
elif selected == "Workout Reminder":

    st.subheader("⏰ Workout Reminder")

    done = st.radio(
        "Did you complete today's workout?",
        ["Yes", "No"]
    )

    if done == "No":

        st.error("Workout Pending")

        st.warning("Consistency Score Reduced")

    else:

        st.success("Workout streak maintained")

# ---------------- CHATBOT ----------------
elif selected == "AI Chatbot":

    st.subheader("🤖 AI Fitness Coach")

    user = st.text_input("Ask Fitness Question")

    if user:

        q = user.lower()

        if "weight" in q:

            ans = "Maintain calorie deficit and cardio workouts."

        elif "muscle" in q:

            ans = "Increase protein intake and strength training."

        elif "diet" in q:

            ans = "Eat balanced meals with hydration and protein."

        else:

            ans = "Stay consistent and trust the process."

        st.success(ans)

# ---------------- FOOD IMAGE ----------------
elif selected == "Food Upload":

    st.subheader("🍎 Food Image Upload")

    food = st.file_uploader(
        "Upload Food Image",
        type=["jpg", "png", "jpeg"]
    )

    if food:

        st.image(food, width=300)

        st.success("Food image uploaded successfully")

# ---------------- PDF UPLOAD ----------------
elif selected == "PDF Upload":

    st.subheader("📄 Upload Fitness Report")

    pdf = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    if pdf:

        st.success("Fitness report uploaded successfully")

# ---------------- ANALYTICS ----------------
elif selected == "Analytics":

    st.subheader("📈 Weekly Analytics")

    data = pd.DataFrame({
        "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        "Calories": [300, 450, 520, 410, 650, 580, 490]
    })

    fig = px.line(
        data,
        x="Day",
        y="Calories",
        markers=True,
        title="Calories Burned"
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="white"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.info("Consistency Score: 91%")

# ---------------- FOOTER ----------------
st.markdown("---")

st.caption(
    "AI Gym Assistant Pro | Python + Streamlit"
)
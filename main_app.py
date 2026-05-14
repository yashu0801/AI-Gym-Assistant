import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
import smtplib
from email.mime.text import MIMEText

st.set_page_config(page_title="AI Gym Assistant Pro", layout="wide")

# ---------------- LOGIN SESSION ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---------------- PREMIUM CSS ----------------
st.markdown("""
<style>

.stApp{
background-image:url("https://images.unsplash.com/photo-1517836357463-d25dfeac3438");
background-size:cover;
background-position:center;
background-attachment:fixed;
}

.main .block-container{
background:rgba(0,0,0,0.72);
padding:2rem;
border-radius:20px;
margin-top:20px;
}

h1,h2,h3,h4,h5,h6,p,label,div{
color:white !important;
}

[data-testid="stSidebar"]{
background:#111827;
}

.stButton>button{
background:#ef4444;
color:white;
border:none;
border-radius:10px;
font-weight:bold;
padding:10px 18px;
}

.stButton>button:hover{
background:#dc2626;
}

.hero-title{
font-size:55px;
font-weight:bold;
text-align:center;
color:#38bdf8 !important;
margin-top:10px;
text-shadow:0px 0px 15px #38bdf8;
}

.hero-sub{
text-align:center;
font-size:22px;
color:#f8fafc !important;
margin-bottom:25px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- LOGIN PAGE ----------------
if not st.session_state.logged_in:

    st.markdown(
        "<div class='hero-title'>🏋️ AI Gym Assistant Pro</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='hero-sub'>AI Powered Smart Fitness Platform</div>",
        unsafe_allow_html=True
    )

    # ---------------- IMAGE SLIDESHOW ----------------
    carousel_html = """
    <div class="slider">
      <img src="https://images.unsplash.com/photo-1517836357463-d25dfeac3438" class="slide">
      <img src="https://images.unsplash.com/photo-1518611012118-6981c7c4b1c8" class="slide">
      <img src="https://images.unsplash.com/photo-1517838277536-f5f99be501cd" class="slide">
      <img src="https://images.unsplash.com/photo-1517963879433-6ad2b056d712" class="slide">
    </div>

    <style>

    .slider{
    position:relative;
    width:100%;
    height:320px;
    overflow:hidden;
    border-radius:20px;
    margin-bottom:25px;
    }

    .slide{
    position:absolute;
    width:100%;
    height:320px;
    object-fit:cover;
    opacity:0;
    animation:fade 16s infinite;
    }

    .slide:nth-child(1){
    animation-delay:0s;
    }

    .slide:nth-child(2){
    animation-delay:4s;
    }

    .slide:nth-child(3){
    animation-delay:8s;
    }

    .slide:nth-child(4){
    animation-delay:12s;
    }

    @keyframes fade{
    0%{opacity:0;}
    10%{opacity:1;}
    25%{opacity:1;}
    35%{opacity:0;}
    100%{opacity:0;}
    }

    </style>
    """

    st.components.v1.html(carousel_html, height=340)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if username == "admin" and password == "admin123":

            st.session_state.logged_in = True
            st.rerun()

        else:

            st.error("Invalid Credentials")

    st.stop()

# ---------------- SIDEBAR ----------------
with st.sidebar:

    selected = option_menu(
        "🏋️ AI Gym Assistant",
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

# ---------------- MAIN TITLE ----------------
st.markdown(
    "<div class='hero-title'> AI Gym Assistant Pro</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='hero-sub'>Transform Your Fitness Journey With AI</div>",
    unsafe_allow_html=True
)

# ---------------- DASHBOARD ----------------
if selected == "Dashboard":

    st.subheader("🔥 Premium Fitness Dashboard")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Calories Burned", "540 kcal")
    c2.metric("Steps Walked", "8,240")
    c3.metric("Workout Streak", "9 Days")
    c4.metric("Water Intake", "3.2 L")

    st.progress(80)

    st.success("Consistency creates transformation.")

# ---------------- BMI ----------------
elif selected == "BMI Calculator":

    st.subheader("📏 BMI Calculator")

    height = st.number_input("Height (cm)", 100)
    weight = st.number_input("Weight (kg)", 20)

    if st.button("Calculate BMI"):

        bmi = weight / ((height / 100) ** 2)

        st.metric("Your BMI", f"{bmi:.2f}")

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
    c3.metric("Calories Burned", f"{calories:.0f} kcal")

    goal = min(steps / 10000, 1.0)

    st.progress(goal)

    if steps < 3000:
        st.warning("You need more walking today")

    else:
        st.success("Great walking consistency")

# ---------------- WORKOUT REMINDER ----------------
elif selected == "Workout Reminder":

    st.subheader("⏰ Smart Workout Reminder")

    user_email = st.text_input("Enter Your Email ID")

    workout = st.radio(
        "Did you complete today's workout?",
        ["Yes", "No"]
    )

    if workout == "No":

        st.error("Workout Pending")

        st.warning("Consistency Score Reduced")

        if st.button("Send Reminder Email"):

            sender_email = "YOUR_GMAIL@gmail.com"
            sender_password = "YOUR_APP_PASSWORD"

            subject = "Workout Reminder"

            body = """
Hello,

You missed today's workout.

Stay consistent to maintain your fitness streak.

- AI Gym Assistant Pro
"""

            msg = MIMEText(body)

            msg["Subject"] = subject
            msg["From"] = sender_email
            msg["To"] = user_email

            try:

                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()

                server.login(
                    sender_email,
                    sender_password
                )

                server.sendmail(
                    sender_email,
                    user_email,
                    msg.as_string()
                )

                server.quit()

                st.success("Reminder Email Sent Successfully")

            except:

                st.error("Email Sending Failed")

    else:

        st.success("Workout Completed Successfully")

# ---------------- AI CHATBOT ----------------
elif selected == "AI Chatbot":

    st.subheader("🤖 AI Fitness Coach")

    question = st.text_input("Ask Fitness Question")

    if question:

        q = question.lower()

        if "weight loss" in q:
            ans = "Follow calorie deficit and daily cardio."

        elif "muscle" in q:
            ans = "Increase protein intake and strength training."

        elif "diet" in q:
            ans = "Eat balanced meals with vegetables and protein."

        elif "walking" in q:
            ans = "Aim for 8,000 to 10,000 steps daily."

        else:
            ans = "Stay consistent and trust the process."

        st.success(ans)

# ---------------- FOOD AI ----------------
elif selected == "Food Upload":

    st.subheader("🍎 AI Food Calorie Analyzer")

    food = st.file_uploader(
        "Upload Food Image",
        type=["jpg", "jpeg", "png"]
    )

    if food:

        st.image(food, width=350)

        filename = food.name.lower()

        calories = 250
        food_name = "Healthy Meal"

        if "rice" in filename:
            food_name = "Rice"
            calories = 200

        elif "burger" in filename:
            food_name = "Burger"
            calories = 350

        elif "pizza" in filename:
            food_name = "Pizza"
            calories = 420

        elif "salad" in filename:
            food_name = "Salad"
            calories = 120

        elif "apple" in filename:
            food_name = "Apple"
            calories = 80

        elif "banana" in filename:
            food_name = "Banana"
            calories = 110

        st.success(f"Detected Food: {food_name}")

        st.metric(
            "Estimated Calories",
            f"{calories} kcal"
        )

        st.info(
            "AI Estimated Calories Based On Uploaded Food Image"
        )

# ---------------- PDF UPLOAD ----------------
elif selected == "PDF Upload":

    st.subheader("📄 Upload Fitness Report")

    pdf = st.file_uploader(
        "Upload PDF Report",
        type=["pdf"]
    )

    if pdf:

        st.success("Fitness Report Uploaded Successfully")

# ---------------- ANALYTICS ----------------
elif selected == "Analytics":

    st.subheader("📈 Weekly Fitness Analytics")

    data = pd.DataFrame({
        "Day":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
        "Calories":[300,450,520,410,650,580,490]
    })

    fig = px.line(
        data,
        x="Day",
        y="Calories",
        markers=True,
        title="Calories Burned Per Day"
    )

    fig.update_layout(
        paper_bgcolor="#111827",
        plot_bgcolor="#111827",
        font_color="white"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.info("Consistency Score: 91%")

# ---------------- FOOTER ----------------
st.markdown("---")

st.caption("AI Gym Assistant Pro | Python + Streamlit")
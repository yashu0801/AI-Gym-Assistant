import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Gym Assistant Pro",
    layout="wide"
)

# ---------------- SESSION STATE ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "users" not in st.session_state:
    st.session_state.users = {
        "admin@gmail.com": "admin123"
    }

if "consistency_score" not in st.session_state:
    st.session_state.consistency_score = 75

if "steps" not in st.session_state:
    st.session_state.steps = 0

if "calories_burned" not in st.session_state:
    st.session_state.calories_burned = 0

if "bmi_value" not in st.session_state:
    st.session_state.bmi_value = 0

if "food_result" not in st.session_state:
    st.session_state.food_result = "No food analyzed"

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
background:rgba(0,0,0,0.78);
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
text-shadow:0px 0px 20px #38bdf8;
}

.hero-sub{
text-align:center;
font-size:22px;
margin-bottom:20px;
color:white !important;
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
        "<div class='hero-sub'>Cloud Based Intelligent Fitness Platform</div>",
        unsafe_allow_html=True
    )

    # ---------------- IMAGE SLIDER ----------------
    slider = """
    <div class="slider">
      <img src="https://images.unsplash.com/photo-1517836357463-d25dfeac3438" class="slide">
      <img src="https://images.unsplash.com/photo-1518611012118-6981c7c4b1c8" class="slide">
      <img src="https://images.unsplash.com/photo-1517838277536-f5f99be501cd" class="slide">
    </div>

    <style>

    .slider{
    position:relative;
    width:100%;
    height:300px;
    overflow:hidden;
    border-radius:20px;
    margin-bottom:20px;
    }

    .slide{
    position:absolute;
    width:100%;
    height:300px;
    object-fit:cover;
    opacity:0;
    animation:fade 12s infinite;
    }

    .slide:nth-child(1){animation-delay:0s;}
    .slide:nth-child(2){animation-delay:4s;}
    .slide:nth-child(3){animation-delay:8s;}

    @keyframes fade{
    0%{opacity:0;}
    10%{opacity:1;}
    30%{opacity:1;}
    40%{opacity:0;}
    100%{opacity:0;}
    }

    </style>
    """

    st.components.v1.html(slider, height=320)

    menu = st.radio(
        "Select Option",
        ["Login", "Register"]
    )

    # ---------------- REGISTER ----------------
    if menu == "Register":

        new_email = st.text_input("Email ID")
        new_password = st.text_input(
            "Create Password",
            type="password"
        )

        if st.button("Create Account"):

            st.session_state.users[new_email] = new_password

            st.success("Account Created Successfully")

    # ---------------- LOGIN ----------------
    else:

        email = st.text_input("Email")
        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Login"):

            if (
                email in st.session_state.users
                and
                st.session_state.users[email] == password
            ):

                st.session_state.logged_in = True
                st.session_state.current_user = email

                st.rerun()

            else:

                st.error("Invalid Email or Password")

    st.stop()

# ---------------- SIDEBAR ----------------
with st.sidebar:

    st.success(
        f"Logged in as: {st.session_state.current_user}"
    )

    selected = option_menu(
        "🏋️ AI Gym Assistant",
        [
            "Dashboard",
            "BMI Calculator",
            "Walking Tracker",
            "Workout Reminder",
            "AI Food Analyzer",
            "AI Chatbot",
            "Analytics",
            "Generate Report"
        ],
        icons=[
            "house",
            "heart",
            "activity",
            "bell",
            "image",
            "robot",
            "bar-chart",
            "file-earmark-text"
        ],
        default_index=0
    )

# ---------------- TITLE ----------------
st.markdown(
    "<div class='hero-title'>🏋️ AI Gym Assistant Pro</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='hero-sub'>AI Assisted Smart Health Monitoring System</div>",
    unsafe_allow_html=True
)

# ---------------- DASHBOARD ----------------
if selected == "Dashboard":

    st.subheader("🔥 Smart Fitness Dashboard")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Calories Burned",
        f"{st.session_state.calories_burned:.0f} kcal"
    )

    c2.metric(
        "Daily Steps",
        st.session_state.steps
    )

    c3.metric(
        "Consistency Score",
        f"{st.session_state.consistency_score}%"
    )

    c4.metric(
        "Workout Streak",
        "9 Days"
    )

    st.progress(
        st.session_state.consistency_score / 100
    )

    st.info(
        "Dashboard dynamically updates based on user activities."
    )

# ---------------- BMI CALCULATOR ----------------
elif selected == "BMI Calculator":

    st.subheader("📏 BMI Calculator")

    height = st.number_input(
        "Height (cm)",
        100
    )

    weight = st.number_input(
        "Weight (kg)",
        20
    )

    if st.button("Calculate BMI"):

        bmi = weight / ((height / 100) ** 2)

        st.session_state.bmi_value = bmi

        st.metric(
            "BMI",
            f"{bmi:.2f}"
        )

        if bmi < 18.5:

            st.warning("Underweight")

            st.info("""
Recommended Suggestions:
- Increase protein intake
- Consume healthy calories
- Include nuts, milk, eggs, banana
- Strength training recommended
- Sleep minimum 7-8 hours
""")

        elif bmi < 25:

            st.success("Healthy")

            st.info("""
Recommended Suggestions:
- Maintain balanced diet
- Continue regular workouts
- Drink enough water
- Include cardio + strength training
""")

        elif bmi < 30:

            st.error("Overweight")

            st.info("""
Recommended Suggestions:
- Reduce junk food intake
- Increase walking and cardio
- Maintain calorie deficit
- Avoid sugary drinks
""")

        else:

            st.error("Obese")

            st.info("""
Recommended Suggestions:
- Follow strict calorie control
- Daily cardio recommended
- Avoid processed foods
- Maintain regular exercise
""")

# ---------------- WALKING TRACKER ----------------
elif selected == "Walking Tracker":

    st.subheader("🚶 Smart Walking Tracker")

    steps = st.number_input(
        "Enter Daily Steps",
        0
    )

    distance = (steps * 0.762) / 1000

    calories = steps * 0.04

    st.session_state.steps = steps
    st.session_state.calories_burned = calories

    c1, c2, c3 = st.columns(3)

    c1.metric("Steps", steps)

    c2.metric(
        "Distance",
        f"{distance:.2f} km"
    )

    c3.metric(
        "Calories Burned",
        f"{calories:.0f} kcal"
    )

    if steps >= 8000:

        st.session_state.consistency_score = min(
            st.session_state.consistency_score + 5,
            100
        )

        st.success(
            "Walking goal achieved successfully."
        )

    else:

        st.warning(
            "Daily walking goal not achieved."
        )

# ---------------- WORKOUT REMINDER ----------------
elif selected == "Workout Reminder":

    st.subheader("⏰ Smart Workout Reminder")

    workout = st.radio(
        "Did you complete today's workout?",
        ["Yes", "No"]
    )

    if workout == "No":

        st.error("Workout Pending")

        st.session_state.consistency_score = max(
            st.session_state.consistency_score - 10,
            0
        )

        if st.button("Send Reminder"):

            st.success(
                "Reminder Notification Triggered Successfully"
            )

    else:

        st.success(
            "Workout Completed Successfully"
        )

        st.session_state.consistency_score = min(
            st.session_state.consistency_score + 5,
            100
        )

# ---------------- FOOD ANALYZER ----------------
elif selected == "AI Food Analyzer":

    st.subheader("🍎 AI Food Calorie Analyzer")

    food = st.file_uploader(
        "Upload Food Image",
        type=["jpg", "jpeg", "png"]
    )

    if food:

        st.image(food, width=350)

        filename = food.name.lower()

        food_name = "Unknown Food"
        calories = 250
        category = "Moderate"

        # ---------------- FOOD DATABASE ----------------

        food_database = {

            "pizza": ("Pizza", 420, "Junk Food"),
            "burger": ("Burger", 350, "Fast Food"),
            "salad": ("Salad", 120, "Healthy Food"),
            "apple": ("Apple", 80, "Healthy Food"),
            "rice": ("Rice", 200, "Balanced Meal"),
            "banana": ("Banana", 90, "Healthy Food"),
            "chicken": ("Chicken", 280, "Protein Rich"),
            "egg": ("Egg", 70, "Protein Rich"),
            "fries": ("French Fries", 300, "Junk Food"),
            "sandwich": ("Sandwich", 250, "Balanced Meal"),
            "dosa": ("Dosa", 180, "South Indian Meal"),
            "idli": ("Idli", 120, "Healthy Food"),
            "biryani": ("Biryani", 450, "High Calorie Meal"),
            "cake": ("Cake", 400, "Dessert"),
            "icecream": ("Ice Cream", 320, "Dessert"),
            "paneer": ("Paneer", 260, "Protein Rich"),
            "milk": ("Milk", 130, "Healthy Drink"),
            "juice": ("Fruit Juice", 140, "Healthy Drink"),
            "noodles": ("Noodles", 330, "Fast Food"),
            "oats": ("Oats", 150, "Healthy Food")
        }

        detected = False

        for key in food_database:

            if key in filename:

                food_name, calories, category = food_database[key]

                detected = True

                break

        healthy_foods = [
            "Healthy Food",
            "Protein Rich",
            "Healthy Drink",
            "Balanced Meal"
        ]

        if category in healthy_foods:

            st.session_state.consistency_score = min(
                st.session_state.consistency_score + 5,
                100
            )

        else:

            st.session_state.consistency_score = max(
                st.session_state.consistency_score - 5,
                0
            )

        st.session_state.food_result = food_name

        st.success(
            f"Detected Food: {food_name}"
        )

        st.metric(
            "Estimated Calories",
            f"{calories} kcal"
        )

        st.info(
            f"Food Category: {category}"
        )

        # ---------------- HEALTH SUGGESTIONS ----------------

        if category == "Junk Food":

            st.warning("""
Suggestions:
- Reduce junk food intake
- Increase cardio workouts
- Avoid excessive calories
""")

        elif category == "Protein Rich":

            st.success("""
Suggestions:
- Excellent for muscle growth
- Maintain workout consistency
- Good post-workout nutrition
""")

        elif category == "Healthy Food":

            st.success("""
Suggestions:
- Great nutritional choice
- Helps maintain fitness goals
- Continue balanced diet
""")

        elif category == "Dessert":

            st.warning("""
Suggestions:
- Consume in moderation
- Balance with physical activity
- Avoid excess sugar intake
""")

        else:

            st.info("""
Suggestions:
- Maintain balanced nutrition
- Include regular physical activity
- Drink enough water
""")

        if not detected:

            st.warning("""
Food not clearly recognized.

For better accuracy:
Rename image properly.

Examples:
pizza.jpg
burger.png
salad.jpeg
""")

# ---------------- AI CHATBOT ----------------
elif selected == "AI Chatbot":

    st.subheader("🤖 AI Fitness Coach")

    question = st.text_input(
        "Ask Fitness Question"
    )

    if question:

        q = question.lower()

        if "weight loss" in q:

            ans = """
Follow calorie deficit,
daily cardio,
and hydration.
"""

        elif "muscle" in q:

            ans = """
Increase protein intake
and strength training.
"""

        elif "diet" in q:

            ans = """
Maintain balanced meals
with vegetables and protein.
"""

        elif "walking" in q:

            ans = """
Target 8000-10000 steps daily.
"""

        else:

            ans = """
Maintain consistency,
proper sleep,
and hydration.
"""

        st.success(ans)

# ---------------- ANALYTICS ----------------
elif selected == "Analytics":

    st.subheader("📈 Fitness Analytics")

    score = st.session_state.consistency_score

    data = pd.DataFrame({

        "Category":[
            "Walking",
            "Workout",
            "Diet",
            "Consistency"
        ],

        "Score":[
            min(score,100),
            max(score-5,50),
            max(score-10,40),
            score
        ]
    })

    fig = px.bar(
        data,
        x="Category",
        y="Score",
        title="Fitness Consistency Analysis"
    )

    fig.update_layout(
        paper_bgcolor="#111827",
        plot_bgcolor="#111827",
        font_color="white"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.success(
        f"Overall Consistency Score: {score}%"
    )

# ---------------- GENERATE REPORT ----------------
elif selected == "Generate Report":

    st.subheader("📄 Generate Final Fitness Report")

    bmi = st.session_state.bmi_value
    steps = st.session_state.steps
    calories = st.session_state.calories_burned
    score = st.session_state.consistency_score
    food = st.session_state.food_result

    if bmi < 18.5:
        bmi_status = "Underweight"

    elif bmi < 25:
        bmi_status = "Healthy"

    elif bmi < 30:
        bmi_status = "Overweight"

    else:
        bmi_status = "Obese"

    report = f"""
AI GYM ASSISTANT PRO
---------------------------------

User:
{st.session_state.current_user}

BMI:
{bmi:.2f}

BMI Status:
{bmi_status}

Daily Steps:
{steps}

Calories Burned:
{calories:.0f} kcal

Food Analysis:
{food}

Consistency Score:
{score}%

Health Suggestions:
- Maintain regular workouts
- Drink sufficient water
- Follow balanced diet
- Maintain proper sleep cycle

Project:
AI Powered Fitness Intelligence Platform
"""

    st.text_area(
        "Generated Fitness Report",
        report,
        height=350
    )

    st.download_button(
        label="⬇ Download Report",
        data=report,
        file_name="fitness_report.txt",
        mime="text/plain"
    )

# ---------------- FOOTER ----------------
st.markdown("---")

st.caption(
    "AI Gym Assistant Pro | Python + Streamlit + AI"
)
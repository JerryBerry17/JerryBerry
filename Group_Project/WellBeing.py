import streamlit as st
import pandas as pd
import datetime
import os

# --- Set page configuration ---
st.set_page_config(page_title="Mental Health Well-Being", layout="centered")

# --- Title ---
st.title("🧠 Mental Health & Well-Being Guide")

# --- Introductory Text ---
st.markdown("""
Mental health matters. This simple app helps you take care of your well-being through:
- ✅ Practical tips
- ✅ Daily mood tracking
- ✅ Helpful resources
""")

# --- Sidebar Navigation ---
section = st.sidebar.radio("Navigation", ["💡 Tips", "📋 Mood Tracker", "📚 Resources"])

# --- Tips Section ---
if section == "💡 Tips":
    st.header("💡 Tips to Take Care of Your Mental Health")
    st.markdown("""
- 💤 **Sleep Well** – Aim for 7–9 hours per night.
- 🥗 **Eat Balanced Meals** – Nutrition supports brain function.
- 🏃 **Exercise Regularly** – Just 30 minutes a day can improve your mood.
- 🧘 **Practice Mindfulness** – Meditation and journaling help reduce stress.
- 👥 **Connect with Others** – Talk to friends, family, or support groups.
- 🎨 **Do What You Enjoy** – Spend time on hobbies or creative activities.
- 🛑 **Take Breaks** – It’s okay to say no and rest.
- 🤝 **Seek Help When Needed** – Don’t hesitate to reach out to professionals.
    """)

# --- Mood Tracker Section ---
elif section == "📋 Mood Tracker":
    st.header("📋 Daily Mood Tracker")
    st.markdown("Log your mood daily and reflect on how you're feeling.")

    mood = st.selectbox("How are you feeling today?", [
        "😊 Happy", "😐 Neutral", "😞 Sad", "😡 Angry", "😰 Anxious", "😴 Tired", "🤩 Excited"
    ])
    note = st.text_area("Add any notes (optional):")
    submit = st.button("Submit")

    if submit:
        today = datetime.date.today()
        entry = pd.DataFrame([[today, mood, note]], columns=["Date", "Mood", "Notes"])

        # Check if file exists, then append or create
        if os.path.exists("mood_log.csv"):
            old_data = pd.read_csv("mood_log.csv")
            data = pd.concat([old_data, entry], ignore_index=True)
        else:
            data = entry

        data.to_csv("mood_log.csv", index=False)
        st.success("✅ Mood successfully logged!")

    # Display mood history
    if os.path.exists("mood_log.csv"):
        st.subheader("📅 Mood History")
        mood_data = pd.read_csv("mood_log.csv")
        st.dataframe(mood_data)
    else:
        st.info("No mood logs yet. Start by submitting your first one!")

# --- Resources Section ---
elif section == "📚 Resources":
    st.header("📚 Mental Health Resources")
    st.markdown("""
**Malaysia:**
- ☎️ **Talian Kasih Hotline**: 15999
- ☎️ **Befrienders KL**: 03-7627 2929  
  🌐 [https://www.befrienders.org.my](https://www.befrienders.org.my)

**International:**
- 🌐 [MentalHealth.gov](https://www.mentalhealth.gov/)
- 🌐 [WHO Mental Health](https://www.who.int/health-topics/mental-health)

🧑‍⚕️ **Reminder:** You're not alone. Don't hesitate to reach out for support.
""")

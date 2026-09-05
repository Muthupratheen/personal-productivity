import streamlit as st

# Page settings
st.set_page_config(
    page_title="My Productivity",
    page_icon="🚀",
    layout="wide"
)

# Title
st.title("🚀 My Productivity Dashboard")
st.write("Organize your day and stay productive.")

# Sidebar
st.sidebar.header("📌 Menu")

menu = st.sidebar.radio(
    "Choose an option",
    ["🏠 Home", "📝 Tasks", "📚 Study", "🗒️ Notes"]
)

# HOME
if menu == "🏠 Home":

    st.header("Good Morning! 👋")
    st.write("Let's make today productive.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("📝 Tasks", "0", "Today")

    with col2:
        st.metric("📚 Study", "0 hrs", "Today")

    with col3:
        st.metric("🎯 Progress", "0%", "Daily")

    st.divider()

    st.subheader("🔥 Today's Focus")

    st.info("Start by adding your first task from the Tasks section.")

# TASKS
elif menu == "📝 Tasks":

    st.header("📝 My Tasks")

    task = st.text_input("Enter a task")

    priority = st.selectbox(
        "Priority",
        ["High 🔴", "Medium 🟡", "Low 🟢"]
    )

    if st.button("➕ Add Task"):

        if task:
            st.success(f"Task added: {task}")
        else:
            st.warning("Please enter a task.")

# STUDY
elif menu == "📚 Study":

    st.header("📚 Study Tracker")

    topic = st.text_input("What are you studying?")

    hours = st.number_input(
        "Study hours",
        min_value=0.0,
        max_value=24.0,
        step=0.5
    )

    if st.button("💾 Save Study"):

        if topic:
            st.success(
                f"Studied {topic} for {hours} hours! 🎉"
            )
        else:
            st.warning("Please enter a topic.")

# NOTES
elif menu == "🗒️ Notes":

    st.header("🗒️ Quick Notes")

    note = st.text_area(
        "Write your note here..."
    )

    if st.button("💾 Save Note"):

        if note:
            st.success("Note saved! ✅")
        else:
            st.warning("Please write something.")

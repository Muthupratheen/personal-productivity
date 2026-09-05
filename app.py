import streamlit as st

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="My Productivity",
    page_icon="🚀",
    layout="wide"
)

# ---------------- SESSION STATE ----------------
if "tasks" not in st.session_state:
    st.session_state.tasks = []

if "study_hours" not in st.session_state:
    st.session_state.study_hours = 0.0

if "notes" not in st.session_state:
    st.session_state.notes = []

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

section[data-testid="stSidebar"] {
    width: 300px !important;
}

section[data-testid="stSidebar"] .stRadio label {
    font-size: 21px !important;
    padding: 10px 5px !important;
}

section[data-testid="stSidebar"] h2 {
    font-size: 27px !important;
}

.stButton button {
    font-size: 17px;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("🚀 My Productivity Dashboard")
st.write("Organize your day and stay productive.")

# ---------------- SIDEBAR ----------------
st.sidebar.header("📌 Menu")

menu = st.sidebar.radio(
    "Choose an option",
    ["🏠 Home", "📝 Tasks", "📚 Study", "🗒️ Notes"]
)

# =================================================
# HOME
# =================================================

if menu == "🏠 Home":

    st.header("Good Morning! 👋")
    st.write("Let's make today productive.")

    total_tasks = len(st.session_state.tasks)
    completed_tasks = sum(
        task["completed"] for task in st.session_state.tasks
    )

    if total_tasks > 0:
        progress = int((completed_tasks / total_tasks) * 100)
    else:
        progress = 0

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "📝 Tasks",
            total_tasks,
            "Today"
        )

    with col2:
        st.metric(
            "📚 Study",
            f"{st.session_state.study_hours} hrs",
            "Today"
        )

    with col3:
        st.metric(
            "🎯 Progress",
            f"{progress}%",
            "Daily"
        )

    st.divider()

    st.subheader("🔥 Today's Focus")

    if total_tasks == 0:
        st.info(
            "Start by adding your first task from the Tasks section."
        )
    else:
        st.progress(progress / 100)

        st.write(
            f"**{completed_tasks} of {total_tasks} tasks completed.**"
        )

# =================================================
# TASKS
# =================================================

elif menu == "📝 Tasks":

    st.header("📝 My Tasks")

    task = st.text_input(
        "Enter a task",
        placeholder="Example: Complete Python practice"
    )

    priority = st.selectbox(
        "Priority",
        ["High 🔴", "Medium 🟡", "Low 🟢"]
    )

    if st.button("➕ Add Task"):

        if task.strip():

            st.session_state.tasks.append({
                "task": task,
                "priority": priority,
                "completed": False
            })

            st.success(f"Task added: {task} ✅")

        else:
            st.warning("Please enter a task.")

    st.divider()

    st.subheader("📋 My Task List")

    if len(st.session_state.tasks) == 0:

        st.info("No tasks yet. Add your first task above 👆")

    else:

        for i, item in enumerate(st.session_state.tasks):

            col1, col2, col3 = st.columns([0.08, 0.65, 0.27])

            with col1:

                completed = st.checkbox(
                    "Done",
                    value=item["completed"],
                    key=f"done_{i}",
                    label_visibility="collapsed"
                )

                st.session_state.tasks[i]["completed"] = completed

            with col2:

                if completed:
                    st.markdown(
                        f"~~**{item['task']}**~~"
                    )
                else:
                    st.markdown(
                        f"**{item['task']}**"
                    )

            with col3:

                st.write(item["priority"])

        st.divider()

        completed_count = sum(
            task["completed"]
            for task in st.session_state.tasks
        )

        st.write(
            f"📊 **Progress: {completed_count} / "
            f"{len(st.session_state.tasks)} tasks completed**"
        )

# =================================================
# STUDY
# =================================================

elif menu == "📚 Study":

    st.header("📚 Study Tracker")

    topic = st.text_input(
        "What are you studying?"
    )

    hours = st.number_input(
        "Study hours",
        min_value=0.0,
        max_value=24.0,
        step=0.5
    )

    if st.button("💾 Save Study"):

        if topic:

            st.session_state.study_hours += hours

            st.success(
                f"Studied {topic} for {hours} hours! 🎉"
            )

        else:

            st.warning("Please enter a topic.")

    st.divider()

    st.subheader("📊 Today's Study")

    st.metric(
        "Total Study Hours",
        f"{st.session_state.study_hours} hrs"
    )

# =================================================
# NOTES
# =================================================

elif menu == "🗒️ Notes":

    st.header("🗒️ Quick Notes")

    note = st.text_area(
        "Write your note here..."
    )

    if st.button("💾 Save Note"):

        if note.strip():

            st.session_state.notes.append(note)

            st.success("Note saved! ✅")

        else:

            st.warning("Please write something.")

    st.divider()

    st.subheader("📋 Saved Notes")

    if len(st.session_state.notes) == 0:

        st.info("No notes yet.")

    else:

        for i, saved_note in enumerate(
            st.session_state.notes,
            start=1
        ):

            st.markdown(
                f"**Note {i}:** {saved_note}"
            )

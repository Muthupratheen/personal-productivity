import streamlit as st

st.set_page_config(
    page_title="My Productivity",
    page_icon="🚀",
    layout="wide"
)

# ---------------- LOGIN ----------------

USERNAME = "muthu"
PASSWORD = "Muthu@123"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


if not st.session_state.logged_in:

    st.title("🔐 Login")
    st.write("Welcome to My Productivity Dashboard")

    username = st.text_input(
        "👤 Username",
        placeholder="Enter username"
    )

    password = st.text_input(
        "🔑 Password",
        type="password",
        placeholder="Enter password"
    )

    if st.button("🚀 Login"):

        if username == USERNAME and password == PASSWORD:

            st.session_state.logged_in = True
            st.success("Login successful! 🎉")
            st.rerun()

        else:

            st.error("❌ Invalid username or password")

    st.stop()


# ---------------- MAIN APP ----------------

st.title("🚀 My Productivity Dashboard")

st.write("Welcome back, Muthu! 👋")

st.sidebar.success("✅ Logged in")

if st.sidebar.button("🚪 Logout"):

    st.session_state.logged_in = False
    st.rerun()

st.header("🏠 Home")

st.write("Organize your day and stay productive.")

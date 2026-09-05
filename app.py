import streamlit as st
import re

# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="User Data Collection",
    page_icon="📋",
    layout="centered"
)

# ---------------- TITLE ----------------

st.title("📋 User Data Collection")
st.write("Please enter your details below.")

st.divider()

# ---------------- INPUT FORM ----------------

with st.form("user_form"):

    name = st.text_input(
        "👤 Name",
        placeholder="Enter your name"
    )

    age = st.number_input(
        "🎂 Age",
        min_value=1,
        max_value=120,
        value=18
    )

    location = st.text_input(
        "📍 Location",
        placeholder="Example: Chennai"
    )

    email = st.text_input(
        "📧 Email ID",
        placeholder="example@gmail.com"
    )

    submit = st.form_submit_button(
        "🚀 Submit Details"
    )

# ---------------- EMAIL VALIDATION ----------------

def valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email)


# ---------------- SHOW DATA ----------------

if submit:

    if not name.strip():
        st.error("❌ Please enter your name.")

    elif not location.strip():
        st.error("❌ Please enter your location.")

    elif not email.strip():
        st.error("❌ Please enter your email.")

    elif not valid_email(email):
        st.error("❌ Please enter a valid email address.")

    else:

        st.success("✅ Details submitted successfully!")

        st.divider()

        st.subheader("👤 Your Profile")

        # -------- PROFILE CARD --------

        col1, col2 = st.columns([1, 2])

        with col1:
            st.markdown(
                """
                <div style="
                    background:#e8f7ff;
                    padding:30px;
                    border-radius:20px;
                    text-align:center;
                    font-size:60px;
                ">
                    👤
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:

            st.markdown(
                f"""
                <div style="
                    background:#f8f9fa;
                    padding:20px;
                    border-radius:15px;
                    border:1px solid #ddd;
                ">

                <h2>👋 {name}</h2>

                <p>🎂 <b>Age:</b> {age}</p>

                <p>📍 <b>Location:</b> {location}</p>

                <p>📧 <b>Email:</b> {email}</p>

                </div>
                """,
                unsafe_allow_html=True
            )

        st.divider()

        # -------- METRICS --------

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("🎂 Age", age)

        with col2:
            st.metric("📍 Location", location)

        with col3:
            st.metric("📧 Email", "Verified ✅")

        st.divider()

        st.info(
            f"🎉 Welcome {name}! Your information has been received."
        )

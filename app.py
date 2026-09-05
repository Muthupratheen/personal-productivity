import streamlit as st
import re

# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="Data Collection",
    page_icon="📋",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.profile-card {
    background-color: #ffffff;
    padding: 30px;
    border-radius: 20px;
    border: 1px solid #dddddd;
    min-height: 230px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
}

.profile-name {
    color: #222222 !important;
    font-size: 30px !important;
    font-weight: 700 !important;
    margin-bottom: 20px;
}

.profile-info {
    color: #333333 !important;
    font-size: 19px !important;
    margin: 12px 0px !important;
}

.profile-label {
    color: #555555 !important;
    font-weight: 600 !important;
}

.avatar-card {
    background-color: #e8f7ff;
    padding: 35px;
    border-radius: 20px;
    text-align: center;
    min-height: 230px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.avatar {
    font-size: 100px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# TITLE
# =========================================================

st.title("📋 User Data Collection")

st.write(
    "Enter your details below and create your profile."
)

st.divider()

# =========================================================
# SESSION STATE
# =========================================================

if "submitted" not in st.session_state:
    st.session_state.submitted = False

if "user_data" not in st.session_state:
    st.session_state.user_data = {}

# =========================================================
# EMAIL VALIDATION
# =========================================================

def valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email)


# =========================================================
# USER INPUT FORM
# =========================================================

if not st.session_state.submitted:

    st.subheader("📝 Enter Your Details")

    with st.form("user_data_form"):

        name = st.text_input(
            "👤 Full Name",
            placeholder="Enter your name"
        )

        age = st.number_input(
            "🎂 Age",
            min_value=1,
            max_value=120,
            value=21,
            step=1
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
            "🚀 Submit Details",
            use_container_width=True
        )

    # =====================================================
    # SUBMIT
    # =====================================================

    if submit:

        if not name.strip():

            st.error("❌ Please enter your name.")

        elif not location.strip():

            st.error("❌ Please enter your location.")

        elif not email.strip():

            st.error("❌ Please enter your email ID.")

        elif not valid_email(email):

            st.error("❌ Please enter a valid email address.")

        else:

            # Save user data in session
            st.session_state.user_data = {
                "name": name.strip(),
                "age": age,
                "location": location.strip(),
                "email": email.strip()
            }

            st.session_state.submitted = True

            st.rerun()


# =========================================================
# PROFILE DISPLAY
# =========================================================

else:

    data = st.session_state.user_data

    st.success("✅ Details submitted successfully!")

    st.divider()

    st.subheader("👤 Your Profile")

    # =====================================================
    # PROFILE CARD
    # =====================================================

    col1, col2 = st.columns([1, 2])

    # ---------------- AVATAR ----------------

    with col1:

        st.markdown(
            """
            <div class="avatar-card">
                <div class="avatar">👤</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # ---------------- USER INFORMATION ----------------

    with col2:

        st.markdown(
            f"""
            <div class="profile-card">

                <div class="profile-name">
                    👋 {data["name"]}
                </div>

                <div class="profile-info">
                    🎂 <span class="profile-label">Age:</span>
                    {data["age"]}
                </div>

                <div class="profile-info">
                    📍 <span class="profile-label">Location:</span>
                    {data["location"]}
                </div>

                <div class="profile-info">
                    📧 <span class="profile-label">Email:</span>
                    {data["email"]}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    # =====================================================
    # METRICS
    # =====================================================

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "🎂 Age",
            data["age"]
        )

    with col2:

        st.metric(
            "📍 Location",
            data["location"]
        )

    with col3:

        st.metric(
            "📧 Email",
            "Valid ✅"
        )

    # =====================================================
    # WELCOME MESSAGE
    # =====================================================

    st.divider()

    st.info(
        f"🎉 Welcome, {data['name']}! "
        "Your information has been successfully collected."
    )

    # =====================================================
    # NEW ENTRY
    # =====================================================

    if st.button(
        "🔄 Create New Profile",
        use_container_width=True
    ):

        st.session_state.submitted = False
        st.session_state.user_data = {}

        st.rerun()

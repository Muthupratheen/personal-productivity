import streamlit as st
import re

# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="User Data Collection",
    page_icon="📋",
    layout="wide"
)

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
# TITLE
# =========================================================

st.title("📋 User Data Collection")
st.write("Enter your details below and create your profile.")

st.divider()


# =========================================================
# INPUT FORM
# =========================================================

if not st.session_state.submitted:

    st.subheader("📝 Enter Your Details")

    with st.form("user_form"):

        name = st.text_input(
            "👤 Full Name",
            placeholder="Enter your full name"
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
    # VALIDATION
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

            st.session_state.user_data = {
                "name": name.strip(),
                "age": age,
                "location": location.strip(),
                "email": email.strip()
            }

            st.session_state.submitted = True

            st.rerun()


# =========================================================
# PROFILE
# =========================================================

else:

    data = st.session_state.user_data

    st.success("✅ Details submitted successfully!")

    st.divider()

    st.subheader("👤 Your Profile")

    # =====================================================
    # PROFILE AREA
    # =====================================================

    col1, col2 = st.columns([1, 2])

    # -----------------------------------------------------
    # AVATAR
    # -----------------------------------------------------

    with col1:

        with st.container(border=True):

            st.markdown(
                "<div style='text-align:center;'>"
                "<div style='font-size:100px;'>👤</div>"
                "<h3>Your Profile</h3>"
                "</div>",
                unsafe_allow_html=True
            )

    # -----------------------------------------------------
    # USER DETAILS
    # -----------------------------------------------------

    with col2:

        with st.container(border=True):

            st.subheader(f"👋 {data['name']}")

            st.write(
                f"🎂 **Age:** {data['age']}"
            )

            st.write(
                f"📍 **Location:** {data['location']}"
            )

            st.write(
                f"📧 **Email:** {data['email']}"
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
    # WELCOME
    # =====================================================

    st.divider()

    st.info(
        f"🎉 Welcome, {data['name']}! "
        "Your information has been successfully collected."
    )

    # =====================================================
    # NEW PROFILE
    # =====================================================

    if st.button(
        "🔄 Create New Profile",
        use_container_width=True
    ):

        st.session_state.submitted = False
        st.session_state.user_data = {}

        st.rerun()

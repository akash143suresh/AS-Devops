import streamlit as st

# Page config
st.set_page_config(
    page_title="AS Clicks Registration",
    page_icon="📸",
    layout="wide"
)

# Custom CSS for better UI
st.markdown("""
<style>
.main-title{
    font-size:40px;
    font-weight:bold;
    text-align:center;
    color:#ff4b4b;
}

.subtitle{
    text-align:center;
    font-size:18px;
    color:gray;
}

.success-box{
    background-color:#0e1117;
    padding:25px;
    border-radius:10px;
    text-align:center;
    color:white;
    font-size:22px;
}

.stButton>button{
    background-color:#ff4b4b;
    color:white;
    border-radius:10px;
    height:45px;
    width:100%;
}
</style>
""", unsafe_allow_html=True)

# Session state
if "registered" not in st.session_state:
    st.session_state.registered = False


# Header
st.markdown('<p class="main-title">📸 AS Clicks Organisation</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Join our creative photography community</p>', unsafe_allow_html=True)

st.divider()

# Registration Form
if not st.session_state.registered:

    st.subheader("Registration Form")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")

    with col2:
        city = st.text_input("City")
        experience = st.selectbox(
            "Photography Experience",
            ["Beginner", "Intermediate", "Professional"]
        )
        interest = st.multiselect(
            "Photography Interest",
            ["Wildlife", "Portrait", "Street", "Nature", "Wedding"]
        )

    submit = st.button("Register")

    if submit:
        if name and email:
            st.session_state.registered = True
            st.session_state.name = name
            st.rerun()
        else:
            st.warning("Please fill required fields")


# After registration
else:

    st.markdown(
        f'<div class="success-box">🎉 Congratulations {st.session_state.name}! <br> You just unlocked exclusive AS Clicks Photography Projects!</div>',
        unsafe_allow_html=True
    )

    st.write("")
    st.subheader("📷 Featured Photography Projects")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(
            "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",
            caption="Nature Photography Project",
            use_container_width=True
        )

    with col2:
        st.image(
            "https://images.unsplash.com/photo-1492724441997-5dc865305da7",
            caption="Street Photography Project",
            use_container_width=True
        )

    with col3:
        st.image(
            "https://images.unsplash.com/photo-1504208434309-cb69f4fe52b0",
            caption="Portrait Photography Project",
            use_container_width=True
        )

    st.write("")
    st.success("More exciting projects will be unlocked soon. Stay tuned!")
    
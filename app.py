import streamlit as st

# إعدادات الصفحة
st.set_page_config(
    page_title="Mahmoud & Gharam Engagement",
    page_icon="💍",
    layout="centered"
)

# تصميم خلفية وألوان أنيقة
st.markdown("""
    <style>
    .main {
        background-color: #FAF8F5;
        text-align: center;
    }
    h1 {
        color: #C5A059;
        font-family: 'Georgia', serif;
    }
    h2, h3 {
        color: #333333;
        font-family: 'Georgia', serif;
    }
    .stButton>button {
        background-color: #C5A059;
        color: white;
        border-radius: 12px;
        padding: 10px 25px;
        border: none;
        font-size: 18px;
    }
    </style>
""", unsafe_allow_html=True)

# تأكيد إحتفالي
st.balloons()

# العنوان الرئيسي
st.title("✨ YOU'RE INVITED! ✨")
st.subheader("🗓️ Save The Date for Mahmoud & Gharam's Engagement")

st.write("---")

# عرض الصورة
try:
    st.image("photo.jpg", caption="Mahmoud ❤️ Gharam: Our Engagement", use_container_width=True)
except Exception:
    st.info("📌 Please place 'photo.jpg' in the same folder.")

st.write("---")

# التفاصيل والميعاد (الجمعة 28 أغسطس الساعة 6:00 مساءً)
st.markdown("### 🗓️ Date & Time")
st.markdown("**Friday, August 28, 2026 at 6:00 PM**")

st.markdown("### 📍 Location")
st.markdown("**Bride's House**")

# رابط اللوكيشن الخاص بك
maps_url = "https://maps.app.goo.gl/MzyyiPAiy9kePkDy8"
st.markdown(f'''
    <a href="{maps_url}" target="_blank">
        <button style="background-color: #C5A059; color: white; padding: 12px 24px; border: none; border-radius: 10px; cursor: pointer; font-size: 16px; font-weight: bold;">
            📍 Open Location on Google Maps
        </button>
    </a>
''', unsafe_allow_html=True)

st.write("---")

# عبارات الانتظار بالإنجليزية
st.markdown("### ✨ We Look Forward to Seeing You! ✨")
st.markdown("*Join us to celebrate our special day!*")

st.write("---")

# قسم التهاني والرسائل
st.markdown("### 💖 Congratulations & Best Wishes 💖")

col1, col2 = st.columns(2)
with col1:
    st.info("💕 So happy for you!")
    st.success("💍 Wishing you a lifetime of joy!")
with col2:
    st.warning("🥂 May your future be bright!")
    st.error("❤️ Sending all our love!")

st.write("")

# نموذج كتابة التهنئة للضيوف
with st.form(key='wishes_form'):
    guest_name = st.text_input("Your Name:")
    guest_message = st.text_area("Your Wishes & Message:")
    submit = st.form_submit_button("Send Wishes ✨")

if submit:
    if guest_name and guest_message:
        st.success(f"Thank you, {guest_name}! Your message has been received ❤️")
        st.snow()
    else:
        st.warning("Please enter your name and message!")
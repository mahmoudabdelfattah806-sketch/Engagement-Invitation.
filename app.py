import streamlit as st
import base64

# 1. إعدادات الصفحة
st.set_page_config(
    page_title="Mahmoud & Gharam Engagement",
    page_icon="💍",
    layout="centered"
)

# 2. التنسيق والتصميم الفرحي الفاخر (الشموع، الستائر، وأنيميشن الدبل)
st.markdown("""
    <style>
    /* خلفية دافئة مع تأثير إضاءة الشموع المتلألئة */
    .stApp {
        background: radial-gradient(circle at 50% 30%, #fffbf2 0%, #f4ebd9 60%, #e6d3b7 100%);
        font-family: 'Georgia', serif;
    }

    /* أنيميشن الستائر البيضاء الحريرة فور فتح الصفحة */
    @keyframes curtainOpenLeft {
        0% { transform: translateX(0); }
        100% { transform: translateX(-100%); visibility: hidden; }
    }
    @keyframes curtainOpenRight {
        0% { transform: translateX(0); }
        100% { transform: translateX(100%); visibility: hidden; }
    }

    .curtain-left, .curtain-right {
        position: fixed;
        top: 0;
        width: 50%;
        height: 100%;
        background: linear-gradient(90deg, #ffffff 0%, #f7f7f7 80%, #e0e0e0 100%);
        z-index: 9999;
        box-shadow: 5px 0 25px rgba(0,0,0,0.15);
        pointer-events: none;
    }
    .curtain-left {
        left: 0;
        animation: curtainOpenLeft 2.2s ease-in-out 0.5s forwards;
    }
    .curtain-right {
        right: 0;
        animation: curtainOpenRight 2.2s ease-in-out 0.5s forwards;
    }

    /* عناوين وديكورات مذهبة */
    h1 {
        color: #D4AF37;
        font-family: 'Georgia', serif;
        font-size: 42px;
        text-shadow: 1px 1px 3px rgba(212, 175, 55, 0.3);
    }
    h2, h3 {
        color: #4A3B32;
        font-family: 'Georgia', serif;
    }

    /* أنيميشن كرتوني لإلباس الخواتم */
    @keyframes ringPulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.15) rotate(5deg); }
        100% { transform: scale(1); }
    }
    @keyframes floatHearts {
        0% { opacity: 0; transform: translateY(10px); }
        50% { opacity: 1; transform: translateY(-10px); }
        100% { opacity: 0; transform: translateY(-25px); }
    }

    .couple-animation-box {
        background: rgba(255, 255, 255, 0.6);
        border: 2px solid #D4AF37;
        border-radius: 20px;
        padding: 20px;
        margin: 20px auto;
        box-shadow: 0 8px 20px rgba(212, 175, 55, 0.2);
        max-width: 400px;
    }
    .chibi-avatar {
        font-size: 55px;
        display: inline-block;
    }
    .ring-icon {
        font-size: 35px;
        display: inline-block;
        animation: ringPulse 2s infinite ease-in-out;
        margin: 0 10px;
    }
    .floating-heart {
        font-size: 20px;
        color: #e74c3c;
        animation: floatHearts 2.5s infinite ease-in-out;
    }

    /* تنسيق الأزرار الذهبية */
    .stButton>button {
        background: linear-gradient(45deg, #D4AF37, #AA7C11);
        color: white;
        border-radius: 25px;
        padding: 12px 30px;
        border: none;
        font-size: 18px;
        box-shadow: 0 4px 15px rgba(212, 175, 55, 0.4);
    }
    </style>

    <!-- عناصر الستائر المتحركة -->
    <div class="curtain-left"></div>
    <div class="curtain-right"></div>
""", unsafe_allow_html=True)

# 3. احتفالية البلونات
st.balloons()

# 4. العنوان الفرحي والأسماء
st.markdown("<h1 style='text-align: center;'>👑 YOU'RE INVITED 👑</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #AA7C11;'>Save The Date For The Engagement Of</h3>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; font-size: 48px;'>✨ Mahmoud & Gharam ✨</h1>", unsafe_allow_html=True)

# أنيميشن العريسين وتبديل الدبل (أنمي/كرتون)
st.markdown("""
    <div class="couple-animation-box" style="text-align: center;">
        <div style="height: 20px;">
            <span class="floating-heart">❤️</span>
            <span class="floating-heart" style="animation-delay: 0.8s;">✨</span>
            <span class="floating-heart" style="animation-delay: 1.5s;">💖</span>
        </div>
        <div>
            <span class="chibi-avatar">🤵🏻‍♂️</span>
            <span class="ring-icon">💍</span>
            <span class="chibi-avatar">👰🏻‍♀️</span>
        </div>
        <p style="color: #8B6508; font-weight: bold; margin-top: 8px; font-size: 15px;">
            Putting a ring on it forever ✨
        </p>
    </div>
""", unsafe_allow_html=True)

st.write("---")

# 🎵 مشغل الموسيقى المضمون
st.markdown("<h4 style='text-align: center; color: #D4AF37;'>🎵 Play Background Music 🎵</h4>", unsafe_allow_html=True)
try:
    audio_file = open('music.mp3', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3')
except Exception:
    st.info("📌 Music file 'music.mp3' not found.")

st.write("---")

# 5. عرض الصورة
try:
    st.image("photo.jpg", caption="Mahmoud ❤️ Gharam", use_container_width=True)
except Exception:
    st.info("📌 Please place 'photo.jpg' in the same folder.")

st.write("---")

# 6. الموعد والمكان
st.markdown("### 🕯️ Date & Time")
st.markdown("#### **Friday, August 28, 2026 at 6:00 PM**")

st.markdown("### 📍 Venue")
st.markdown("#### **Bride's House**")

# زرار اللوكيشن الذهبي
maps_url = "https://maps.app.goo.gl/MzyyiPAiy9kePkDy8"
st.markdown(f'''
    <div style="text-align: center; margin: 25px 0;">
        <a href="{maps_url}" target="_blank">
            <button style="background: linear-gradient(45deg, #D4AF37, #B8860B); color: white; padding: 14px 28px; border: none; border-radius: 30px; cursor: pointer; font-size: 18px; font-weight: bold; box-shadow: 0px 4px 12px rgba(0,0,0,0.15);">
                📍 Open Location on Google Maps
            </button>
        </a>
    </div>
''', unsafe_allow_html=True)

st.write("---")

# 7. الرسالة والمباركات
st.markdown("### 💖 We Look Forward to Celebrating With You! 💖")
st.markdown("*Your presence will make our day truly complete!*")

st.write("---")

st.markdown("### 💌 Send Your Wishes & Blessings 💌")

with st.form(key='wishes_form'):
    guest_name = st.text_input("Your Name:")
    guest_message = st.text_area("Your Wishes:")
    submit = st.form_submit_button("Send Love ✨")

if submit:
    if guest_name and guest_message:
        st.success(f"Thank you, {guest_name}! Your lovely message has been sent ❤️")
        st.snow()
    else:
        st.warning("Please enter your name and message!")

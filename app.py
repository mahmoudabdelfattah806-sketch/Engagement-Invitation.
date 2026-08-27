import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(
    page_title="Mahmoud & Gharam Engagement",
    page_icon="💍",
    layout="centered"
)

# 2. التصميم الفاخر (الخلفية الداكنة، الستائر البطئية، أنيميشن الخاتم)
st.markdown("""
    <style>
    /* خلفية داكنة ملكية (Dark Luxury Theme) */
    .stApp {
        background: radial-gradient(circle at 50% 30%, #1a162b 0%, #0d0b18 60%, #05040a 100%);
        color: #f0f0f0;
        font-family: 'Georgia', serif;
    }

    /* أنيميشن الستائر البيضاء - بطيئة وانسيابية (4 ثوانٍ) */
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
        background: linear-gradient(90deg, #ffffff 0%, #eaeaea 80%, #dcdcdx 100%);
        z-index: 9999;
        box-shadow: 10px 0 30px rgba(0,0,0,0.5);
        pointer-events: none;
    }
    .curtain-left {
        left: 0;
        animation: curtainOpenLeft 4s ease-in-out 0.8s forwards;
    }
    .curtain-right {
        right: 0;
        animation: curtainOpenRight 4s ease-in-out 0.8s forwards;
    }

    /* العناوين المذهبة */
    h1 {
        color: #F3E5AB;
        font-family: 'Georgia', serif;
        font-size: 44px;
        text-shadow: 0px 2px 10px rgba(243, 229, 171, 0.4);
    }
    h2, h3, h4 {
        color: #E6C687;
        font-family: 'Georgia', serif;
    }

    /* أنيميشن كرتوني ضخم ومتحرك لإلباس الخواتم */
    @keyframes groomMove {
        0%, 100% { transform: translateX(0) rotate(0deg); }
        50% { transform: translateX(15px) rotate(5deg); }
    }
    @keyframes brideMove {
        0%, 100% { transform: translateX(0) rotate(0deg); }
        50% { transform: translateX(-15px) rotate(-5deg); }
    }
    @keyframes ringSparkle {
        0% { transform: scale(1) rotate(0deg); filter: drop-shadow(0 0 2px #fff); }
        50% { transform: scale(1.4) rotate(15deg); filter: drop-shadow(0 0 12px #FFD700); }
        100% { transform: scale(1) rotate(0deg); filter: drop-shadow(0 0 2px #fff); }
    }
    @keyframes floatUp {
        0% { opacity: 0; transform: translateY(15px) scale(0.8); }
        50% { opacity: 1; transform: translateY(-15px) scale(1.2); }
        100% { opacity: 0; transform: translateY(-35px) scale(0.8); }
    }

    .couple-card {
        background: rgba(255, 255, 255, 0.05);
        border: 2px solid #D4AF37;
        border-radius: 25px;
        padding: 30px 15px;
        margin: 25px auto;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        max-width: 450px;
        backdrop-filter: blur(5px);
    }
    .chibi-groom {
        font-size: 75px;
        display: inline-block;
        animation: groomMove 3s ease-in-out infinite;
    }
    .chibi-bride {
        font-size: 75px;
        display: inline-block;
        animation: brideMove 3s ease-in-out infinite;
    }
    .ring-animated {
        font-size: 50px;
        display: inline-block;
        margin: 0 15px;
        animation: ringSparkle 2s infinite ease-in-out;
    }
    .heart-effect {
        font-size: 26px;
        display: inline-block;
        animation: floatUp 2.2s infinite ease-in-out;
    }

    /* زرار الإرسال */
    .stButton>button {
        background: linear-gradient(45deg, #D4AF37, #AA7C11);
        color: white;
        border-radius: 25px;
        padding: 12px 30px;
        border: none;
        font-size: 18px;
        box-shadow: 0 4px 15px rgba(212, 175, 55, 0.3);
    }
    </style>

    <!-- الستائر المتنقلة -->
    <div class="curtain-left"></div>
    <div class="curtain-right"></div>
""", unsafe_allow_html=True)

# 3. احتفالية البلونات
st.balloons()

# 4. العنوان الفرحي والأسماء
st.markdown("<h1 style='text-align: center;'>👑 YOU'RE INVITED 👑</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #E6C687;'>Save The Date For The Engagement Of</h3>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; font-size: 52px;'>✨ Mahmoud & Gharam ✨</h1>", unsafe_allow_html=True)

# 5. أنيميشن العريسين الضخم
st.markdown("""
    <div class="couple-card" style="text-align: center;">
        <div style="height: 30px; margin-bottom: 5px;">
            <span class="heart-effect">💖</span>
            <span class="heart-effect" style="animation-delay: 0.7s;">✨</span>
            <span class="heart-effect" style="animation-delay: 1.4s;">❤️</span>
        </div>
        <div>
            <span class="chibi-groom">🤵🏻‍♂️</span>
            <span class="ring-animated">💍</span>
            <span class="chibi-bride">👰🏻‍♀️</span>
        </div>
        <p style="color: #F3E5AB; font-weight: bold; margin-top: 15px; font-size: 18px; letter-spacing: 1px;">
            Forever Starts Today ✨
        </p>
    </div>
""", unsafe_allow_html=True)

st.write("---")

# 🎵 مشغل الموسيقى
st.markdown("<h4 style='text-align: center; color: #F3E5AB;'>🎵 Play Background Music 🎵</h4>", unsafe_allow_html=True)
try:
    audio_file = open('music.mp3', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3')
except Exception:
    st.info("📌 Music file 'music.mp3' not found.")

st.write("---")

# 6. عرض الصورة
try:
    st.image("photo.jpg", caption="Mahmoud ❤️ Gharam", use_container_width=True)
except Exception:
    st.info("📌 Please place 'photo.jpg' in the same folder.")

st.write("---")

# 7. الموعد والمكان
st.markdown("### 🗓️ Date & Time")
st.markdown("#### **Friday, August 28, 2026 at 6:00 PM**")

st.markdown("### 📍 Venue")
st.markdown("#### **Bride's House**")

# زرار اللوكيشن الذهبي
maps_url = "https://maps.app.goo.gl/MzyyiPAiy9kePkDy8"
st.markdown(f'''
    <div style="text-align: center; margin: 25px 0;">
        <a href="{maps_url}" target="_blank">
            <button style="background: linear-gradient(45deg, #D4AF37, #B8860B); color: white; padding: 14px 28px; border: none; border-radius: 30px; cursor: pointer; font-size: 18px; font-weight: bold; box-shadow: 0px 4px 15px rgba(212,175,55,0.3);">
                📍 Open Location on Google Maps
            </button>
        </a>
    </div>
''', unsafe_allow_html=True)

st.write("---")

# 8. المباركات
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

import streamlit as st
import base64

# 1. إعدادات الصفحة
st.set_page_config(
    page_title="Mahmoud & Gharam Engagement",
    page_icon="💍",
    layout="centered"
)

# -------------------------------------------------------------
# 🎵 تشغيل الموسيقى عند أول لمسة أو حركة في الصفحة (Smart Autoplay)
# -------------------------------------------------------------
def get_audio_html(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            return f"""
                <audio id="bg-music" loop style="display:none;">
                    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
                <script>
                    function playAudio() {{
                        var audio = document.getElementById("bg-music");
                        if (audio) {{
                            audio.play().then(function() {{
                                // تم التشغيل بنجاح، إزالة المستمعين
                                removeListeners();
                            }}).catch(function(e) {{
                                console.log("Waiting for user interaction");
                            }});
                        }}
                    }}

                    function removeListeners() {{
                        document.removeEventListener("click", playAudio);
                        document.removeEventListener("touchstart", playAudio);
                        document.removeEventListener("scroll", playAudio);
                    }}

                    // تشغيل الصوت فوراً أو عند أول حركة/لمسة للضيف
                    document.addEventListener("DOMContentLoaded", playAudio);
                    document.addEventListener("click", playAudio);
                    document.addEventListener("touchstart", playAudio);
                    document.addEventListener("scroll", playAudio);
                </script>
            """
    except Exception:
        return ""

music_html = get_audio_html("music.mp3")
if music_html:
    st.components.v1.html(music_html, height=0)
# -------------------------------------------------------------

# 2. التنسيق والتصميم الفرحي الفاخر
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #fffcf9 0%, #f7eae1 100%);
        text-align: center;
        font-family: 'Georgia', serif;
    }
    h1 {
        color: #D4AF37;
        font-family: 'Georgia', serif;
        font-size: 42px;
        text-shadow: 1px 1px 2px #d4af3733;
    }
    h2, h3 {
        color: #4A3B32;
        font-family: 'Georgia', serif;
    }
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
""", unsafe_allow_html=True)

# 3. احتفالية البلونات
st.balloons()

# 4. العنوان الفرحي والأسماء
st.markdown("<h1 style='text-align: center;'>👑 YOU'RE INVITED 👑</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #AA7C11;'>Save The Date For The Engagement Of</h3>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; font-size: 48px;'>✨ Mahmoud & Gharam ✨</h1>", unsafe_allow_html=True)

st.write("---")

# 5. عرض الصورة
try:
    st.image("photo.jpg", caption="Mahmoud ❤️ Gharam", use_container_width=True)
except Exception:
    st.info("📌 Please place 'photo.jpg' in the same folder.")

st.write("---")

# 6. الموعد والمكان
st.markdown("### 🗓️ Date & Time")
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

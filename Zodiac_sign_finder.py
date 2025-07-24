import streamlit as st
from datetime import datetime
import base64
import os

def set_background(image_path):
    """
    Set a local image as the background for the Streamlit app.
    """
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            encoded = base64.b64encode(img_file.read()).decode()
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/png;base64,{encoded}");
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
# Background image path 
set_background("Unlock the Mysteries of the Zodiac Signs_ A Cosmic Journey Awaits(1).jpeg")

# --- Zodiac Descriptions ---
zodiac_info = {
    "Capricorn": "♑ Capricorn — Capricorns are responsible, disciplined, and have strong self-control.",
    "Aquarius": "♒ Aquarius — Aquarians are independent, progressive, and love intellectual conversations.",
    "Pisces": "♓ Pisces — Pisces are empathetic, artistic, and deeply emotional individuals.",
    "Aries": "♈ Aries — Aries are bold, ambitious, and full of energy.",
    "Taurus": "♉ Taurus — Taurus individuals are reliable, patient, and love stability.",
    "Gemini": "♊ Gemini — Geminis are curious, adaptable, and great communicators.",
    "Cancer": "♋ Cancer — Cancers are nurturing, protective, and highly intuitive.",
    "Leo": "♌ Leo — Leos are confident, charismatic, and natural-born leaders.",
    "Virgo": "♍ Virgo — Virgos are analytical, detail-oriented, and perfectionists.",
    "Libra": "♎ Libra — Libras seek balance, are diplomatic, and value harmony.",
    "Scorpio": "♏ Scorpio — Scorpios are passionate, mysterious, and deeply emotional.",
    "Sagittarius": "♐ Sagittarius — Sagittarians are adventurous, optimistic, and love freedom."
}

# --- Zodiac Logic ---
def get_zodiac_sign(day, month):
    zodiac_signs = [
        ("Capricorn", (1, 19)), ("Aquarius", (2, 18)), ("Pisces", (3, 20)),
        ("Aries", (4, 19)), ("Taurus", (5, 20)), ("Gemini", (6, 20)),
        ("Cancer", (7, 22)), ("Leo", (8, 22)), ("Virgo", (9, 22)),
        ("Libra", (10, 22)), ("Scorpio", (11, 21)), ("Sagittarius", (12, 21)),
        ("Capricorn", (12, 31))
    ]
    for sign, (m, d) in zodiac_signs:
        if (month == m and day <= d) or (month < m):
            return sign
    return "Capricorn"

# --- "Popup-style" Title ---
st.markdown("""
    <div style='
        background-color: #fbe8f4;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
        text-align: center;
        font-size: 32px;
        font-weight: bold;
        color: #6a1b9a;
    '>
        ✨ Welcome to the Zodiac Sign Finder ✨
    </div>
""", unsafe_allow_html=True)

st.write("Enter your birthdate to discover your zodiac sign and its meaning.")

birthdate = st.date_input("📅 Select your birthdate:", min_value=datetime(1900, 1, 1))

if st.button("🔍 Find My Zodiac Sign"):
    if birthdate:
        sign = get_zodiac_sign(birthdate.day, birthdate.month)
        description = zodiac_info.get(sign, "No description available.")

        st.markdown(f"""
            <div style='
                margin-top: 30px;
                padding: 20px;
                background-color: #000000;
                border-left: 8px solid #f57c00;
                border-radius: 10px;
                font-size: 22px;
                line-height: 1.6;
                box-shadow: 2px 2px 12px rgba(0,0,0,0.1);
            '>
                🌟 <strong>Your Zodiac Sign is: {sign}</strong><br>
                📖 {description}
            </div>
        """, unsafe_allow_html=True)

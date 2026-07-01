"""
NeonUI Demo App 💜
Showcases ALL themes with a live switcher!
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from neonui import apply_theme

# ─── PAGE CONFIG ───
st.set_page_config(
    page_title="NeonUI Demo 🎨",
    page_icon="🎨",
    layout="wide",
)

# ─── SIDEBAR THEME SWITCHER ───
with st.sidebar:
    st.markdown("### 🎨 Theme Switcher")

    theme_options = {
        "💜 Cosmic Purple": "cosmic_purple",
        "🕹️ Neon Tokyo": "neon_tokyo",
        "🍓 Strawberry Matcha": "strawberry_matcha",
        "🌈 Aurora": "aurora",
        "🌙 Midnight": "midnight",
    }

    selected_display = st.radio(
        "Choose a theme:",
        list(theme_options.keys()),
        index=0
    )

    selected_theme = theme_options[selected_display]

    st.markdown("---")
    st.markdown(f"**Current:** `{selected_theme}`")
    st.markdown("---")
    st.markdown("### 💜 About NeonUI")
    st.markdown("Beautiful Streamlit components with neon aesthetics.")
    st.markdown("Made with 💜 by Vivi")

# ─── APPLY SELECTED THEME ───
apply_theme(selected_theme)

# ─── HEADER ───
st.title(f"🎨 NeonUI - {selected_display}")
st.markdown("### *Streamlit apps that don't look like Streamlit apps*")

st.markdown("---")

# ─── WIDGET SHOWCASE ───
st.header("🎨 Widget Showcase")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Text Input")
    name = st.text_input("What's your name?", placeholder="Enter your name...")

    st.subheader("Text Area")
    bio = st.text_area("Tell us about yourself", placeholder="Write something amazing...", height=100)

    st.subheader("Select Box")
    fav = st.selectbox(
        "Favorite color?",
        ["💜 Purple", "🌈 Rainbow", "🍓 Pink", "🌙 Silver", "🌊 Cyan"]
    )

with col2:
    st.subheader("Buttons")
    if st.button("👋 Say Hello"):
        if name:
            st.success(f"Hello, {name}! ✨")
        else:
            st.warning("Enter your name first! 🥺")

    if st.button("💜 Show My Info", type="primary"):
        if name and bio:
            st.info(f"**{name}** says: *{bio}*")
        elif name:
            st.info(f"Hi **{name}**! Tell us more about yourself in the text area! 📝")
        else:
            st.warning("Fill in your name and bio first! 🌟")

    st.subheader("Slider")
    magic = st.slider("Magic Level", 0, 100, 75, key="magic_slider")

    if magic >= 90:
        st.markdown("🔥 **Maximum magic unlocked!**")
    elif magic >= 70:
        st.markdown("✨ *Feeling magical!*")
    elif magic >= 40:
        st.markdown("💫 Getting warmer...")
    else:
        st.markdown("😴 Need more magic!")

    st.subheader("Radio")
    mood = st.radio("Current mood?", ["✨ Magical", "💜 Cozy", "🌟 Stellar"], horizontal=True)
    st.caption(f"You're feeling {mood}!")

st.markdown("---")

# ─── METRICS ───
st.header("📊 Metrics")

m1, m2, m3, m4 = st.columns(4)
m1.metric("Users", "1,234", "+12%")
m2.metric("Stars", "567", "+45")
m3.metric("Downloads", "8,910", "+8%")
m4.metric("Revenue", "$12K", "-3%")

st.markdown("---")

# ─── TABS ───
st.header("📁 Tabs")

tab1, tab2, tab3 = st.tabs(["📊 Overview", "🎨 Design", "💜 About"])

with tab1:
    st.write("This is the overview tab with all the important info!")

with tab2:
    st.write("Design tab showcasing our beautiful theme!")

with tab3:
    st.write("About NeonUI - Made with 💜 by Vivi")

st.markdown("---")

# ─── ALERTS ───
st.header("🔔 Alerts")

st.success("✅ Success message - everything works!")
st.info("💡 Info message - here's something useful")
st.warning("⚠️ Warning message - be careful!")
st.error("❌ Error message - something went wrong")

st.markdown("---")

# ─── EXPANDER ───
st.header("📁 Expander")

with st.expander("Click to expand"):
    st.write("Hidden content revealed! 🎉")
    st.code("print('Hello, NeonUI!')", language="python")

st.markdown("---")

# ─── FOOTER ───
st.markdown(f"""
<div style="text-align: center; padding: 2rem 0; opacity: 0.7;">
    Made with 💜 using <strong>NeonUI</strong> · Theme: {selected_display}
</div>
""", unsafe_allow_html=True)
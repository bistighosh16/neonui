<div align="center">

# 🎨 NeonUI

### *Streamlit apps that don't look like Streamlit apps.*

Beautiful, ready-to-use Streamlit components with **5 stunning themes** and glassmorphism magic. ✨

[![PyPI version](https://img.shields.io/pypi/v/neonui?color=B24BF3&style=for-the-badge)](https://pypi.org/project/neonui/)
[![Python](https://img.shields.io/badge/Python-3.8+-4CC9F0?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF6EC7?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-7FFF9E?style=for-the-badge)](LICENSE)
[![Made with Love](https://img.shields.io/badge/Made%20with-💜-B24BF3?style=for-the-badge)](https://github.com/bistighosh16)

(**[✨ Live Demo](https://neonui-demo.streamlit.app/)**) · **[📖 Documentation](#-quick-start)** · **[🎨 Themes](#-themes)** · **[💜 Made by Vivi](https://github.com/bistighosh16)**

</div>

---

## 🌟 Why NeonUI?

Ever built a Streamlit app and thought *"this looks... functional but boring"?* 😅

**NeonUI transforms your Streamlit apps into stunning, production-ready interfaces with just ONE line of code.** No CSS knowledge needed. No component headaches. Just beautiful UIs, instantly.

```python
from neonui import apply_theme

apply_theme("cosmic_purple")  # That's it. Seriously. ✨
🎨 Themes
Choose from 5 gorgeous, hand-crafted themes:

Theme	Vibe	Best For
💜 Cosmic Purple	Deep space with starry backgrounds and electric purple glows	AI apps, chatbots, futuristic dashboards
🕹️ Neon Tokyo	Cyberpunk arcade with CRT scanlines and pixel fonts	Gaming apps, developer tools, retro projects
🍓 Strawberry Matcha	Cute cottagecore with sage green and pink pastels	Personal apps, journals, cozy tools
🌈 Aurora	Northern lights with flowing rainbow gradients	Creative tools, art apps, portfolio sites
🌙 Midnight	Elegant minimal dark with silver accents	Business dashboards, luxury apps, portfolios
🚀 Installation
Bash

pip install neonui
That's it! You're ready to make beautiful apps! ✨

⚡ Quick Start
1. Basic Usage
Python

import streamlit as st
from neonui import apply_theme

# Apply your favorite theme
apply_theme("cosmic_purple")

# Build your app as normal - it'll look STUNNING! 
st.title("My Beautiful App")
st.write("This looks amazing now! 💜")

if st.button("Click me"):
    st.success("So pretty!")
2. Available Themes
Python

from neonui import apply_theme

apply_theme("cosmic_purple")       # 💜 Deep space vibes
apply_theme("neon_tokyo")          # 🕹️ Cyberpunk arcade
apply_theme("strawberry_matcha")   # 🍓 Cute cottagecore
apply_theme("aurora")              # 🌈 Northern lights
apply_theme("midnight")            # 🌙 Elegant dark
3. List All Themes
Python

from neonui import list_themes

themes = list_themes()
print(themes)
# ['cosmic_purple', 'neon_tokyo', 'strawberry_matcha', 'aurora', 'midnight']
4. Get Theme Info
Python

from neonui import get_theme_info

info = get_theme_info("cosmic_purple")
print(info["description"])
print(info["colors"])
🎯 Bonus Utilities
Hide Streamlit Defaults
Python

from neonui import hide_streamlit_defaults

hide_streamlit_defaults()  # Removes menu, footer, header
Inject Custom CSS
Python

from neonui import inject_css

inject_css("""
    .my-custom-class {
        color: purple;
    }
""")
Custom Backgrounds
Python

from neonui import set_page_background

# Solid color
set_page_background(color="#0a0011")

# Gradient
set_page_background(gradient="linear-gradient(135deg, #667eea, #764ba2)")

# Image
set_page_background(image_url="https://example.com/bg.jpg")
💡 Real-World Example
Build a stunning dashboard in seconds:

Python

import streamlit as st
from neonui import apply_theme

apply_theme("aurora")

st.title("📊 My Dashboard")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Revenue", "$12K", "+8%")
col2.metric("Users", "1,234", "+12%")
col3.metric("Growth", "45%", "+5%")
col4.metric("Rating", "4.9", "+0.2")

tab1, tab2 = st.tabs(["📈 Overview", "🎯 Details"])

with tab1:
    st.write("Beautiful, isn't it?")

with tab2:
    if st.button("Take Action", type="primary"):
        st.balloons()
Your app now looks like a premium product! 🚀

🎨 What Makes NeonUI Different?
✨ Zero configuration - Import and apply, that's it!
🎯 Streamlit-native - Works with ALL Streamlit widgets automatically
💜 5 curated themes - Hand-crafted with real design principles
🌐 Google Fonts included - Loaded automatically per theme
📱 Responsive - Looks great on all screen sizes
🔓 MIT License - Free for personal and commercial use
🚫 No dependencies - Just Streamlit, that's it!
⚡ Lightweight - Minimal overhead, maximum beauty

<div align="center">
💜 Cosmic Purple
Deep space vibes with starry backgrounds

🕹️ Neon Tokyo
Cyberpunk arcade with CRT scanlines

🍓 Strawberry Matcha
Cute cottagecore aesthetic

🌈 Aurora
Northern lights with flowing gradients

🌙 Midnight
Elegant minimal luxury

👉 Try the Live Demo to see them all in action!

</div>
🛣️ Roadmap
✅ v0.1.0 (Current)
5 gorgeous themes
Theme switching API
CSS injection utilities
Live demo app
🚧 v0.2.0 (Coming Soon)
Custom components (cards, badges, chat bubbles)
More themes based on community requests
Component-level theme overrides
Animation utilities
🌟 v0.3.0 (Planned)
Dashboard templates
Chart theme integration
Dark/light mode toggle
Theme customization API
🤝 Contributing
Contributions are welcome! Whether it's:

🐛 Bug reports
💡 Feature suggestions
🎨 New theme ideas
📝 Documentation improvements
⭐ Just starring the repo!
Open an issue or PR at github.com/bistighosh16/neonui

📄 License
MIT License © 2025 Vivi

Free to use for personal and commercial projects. Attribution appreciated but not required! 💜

🌟 Show Your Support
If NeonUI made your Streamlit app more beautiful, please consider:

⭐ Starring this repo
🐦 Sharing on Twitter/LinkedIn
☕ Following me on GitHub
<div align="center">
Made with 💜 by Vivi
Because Streamlit apps deserve to look beautiful.

⬆ Back to Top

</div> ```

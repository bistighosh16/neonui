"""
CSS Injector Utility 🎨
Handles injecting custom CSS into Streamlit apps
"""

import streamlit as st


def inject_css(css: str) -> None:
    """
    Inject custom CSS into a Streamlit app.
    
    Args:
        css: Raw CSS string to inject
        
    Example:
        inject_css("h1 { color: purple; }")
    """
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


def inject_html(html: str) -> None:
    """
    Inject raw HTML into a Streamlit app.
    
    Args:
        html: Raw HTML string to inject
        
    Example:
        inject_html("<div class='my-card'>Hello</div>")
    """
    st.markdown(html, unsafe_allow_html=True)


def inject_google_font(font_name: str, weights: list = None) -> None:
    """
    Load a Google Font into the Streamlit app.
    
    Args:
        font_name: Name of the Google Font (e.g., "Orbitron")
        weights: List of weights to load (e.g., [400, 700])
        
    Example:
        inject_google_font("Orbitron", [400, 700, 900])
    """
    if weights:
        weights_str = ";".join(str(w) for w in weights)
        font_url_name = font_name.replace(" ", "+")
        font_link = (
            f"https://fonts.googleapis.com/css2?"
            f"family={font_url_name}:wght@{weights_str}&display=swap"
        )
    else:
        font_url_name = font_name.replace(" ", "+")
        font_link = f"https://fonts.googleapis.com/css2?family={font_url_name}&display=swap"

    html = f'<link href="{font_link}" rel="stylesheet">'
    inject_html(html)


def inject_multiple_fonts(fonts: list) -> None:
    """
    Load multiple Google Fonts at once.
    
    Args:
        fonts: List of font names or (font_name, weights) tuples
        
    Example:
        inject_multiple_fonts([
            "Orbitron",
            ("Press Start 2P", None),
            ("Inter", [400, 600, 700])
        ])
    """
    for font in fonts:
        if isinstance(font, tuple):
            inject_google_font(font[0], font[1])
        else:
            inject_google_font(font)


def hide_streamlit_defaults() -> None:
    """
    Hide default Streamlit UI elements (menu, footer, header).
    Perfect for making apps look like custom products!
    """
    css = """
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}
    """
    inject_css(css)


def set_page_background(color: str = None, gradient: str = None, image_url: str = None) -> None:
    """
    Set a custom background for the entire page.
    
    Args:
        color: Solid background color (e.g., "#0a0011")
        gradient: CSS gradient (e.g., "linear-gradient(135deg, #667eea, #764ba2)")
        image_url: URL to a background image
        
    Example:
        set_page_background(color="#0a0011")
        set_page_background(gradient="linear-gradient(135deg, #667eea, #764ba2)")
    """
    if image_url:
        bg_value = f"url('{image_url}') center/cover no-repeat"
    elif gradient:
        bg_value = gradient
    elif color:
        bg_value = color
    else:
        return

    css = f"""
    .stApp {{
        background: {bg_value} !important;
    }}
    """
    inject_css(css)
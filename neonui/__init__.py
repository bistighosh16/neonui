"""
NeonUI - Beautiful Streamlit Components with Neon Aesthetics
Made with 💜 by Vivi

Streamlit apps that don't look like Streamlit apps.
"""

__version__ = "0.1.0"
__author__ = "Vivi"
__email__ = "bistighosh16@gmail.com"

# Expose the main theme functions at the package level!
from neonui.utils.theme_loader import apply_theme, list_themes, get_theme_info
from neonui.utils.css_injector import (
    inject_css,
    inject_html,
    hide_streamlit_defaults,
    set_page_background,
)

__all__ = [
    "__version__",
    "apply_theme",
    "list_themes",
    "get_theme_info",
    "inject_css",
    "inject_html",
    "hide_streamlit_defaults",
    "set_page_background",
]
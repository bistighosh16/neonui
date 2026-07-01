"""NeonUI Utilities"""

from neonui.utils.css_injector import (
    inject_css,
    inject_html,
    inject_google_font,
    inject_multiple_fonts,
    hide_streamlit_defaults,
    set_page_background,
)

from neonui.utils.theme_loader import (
    apply_theme,
    list_themes,
    get_theme_info,
)

__all__ = [
    "inject_css",
    "inject_html",
    "inject_google_font",
    "inject_multiple_fonts",
    "hide_streamlit_defaults",
    "set_page_background",
    "apply_theme",
    "list_themes",
    "get_theme_info",
]
"""
Theme Loader Utility 🎨
Handles loading and applying complete themes to Streamlit apps
"""

from neonui.utils.css_injector import inject_css, inject_multiple_fonts


# Registry of available themes
AVAILABLE_THEMES = {
    "cosmic_purple": "neonui.themes.cosmic_purple",
    "neon_tokyo": "neonui.themes.neon_tokyo",
    "strawberry_matcha": "neonui.themes.strawberry_matcha",
    "aurora": "neonui.themes.aurora",
    "midnight": "neonui.themes.midnight",
}


def apply_theme(theme_name: str) -> None:
    """
    Apply a complete NeonUI theme to your Streamlit app.
    
    Args:
        theme_name: Name of the theme to apply. Options:
            - "cosmic_purple" (default) 💜
            - "neon_tokyo" 🕹️
            - "strawberry_matcha" 🍓🍵
            - "aurora" 🌈
            - "midnight" 🌙
            
    Example:
        from neonui import apply_theme
        apply_theme("cosmic_purple")
    """
    if theme_name not in AVAILABLE_THEMES:
        available = ", ".join(AVAILABLE_THEMES.keys())
        raise ValueError(
            f"Theme '{theme_name}' not found! "
            f"Available themes: {available}"
        )

    # Dynamically import the theme module
    import importlib
    theme_module = importlib.import_module(AVAILABLE_THEMES[theme_name])

    # Load fonts if the theme specifies them
    if hasattr(theme_module, "FONTS"):
        inject_multiple_fonts(theme_module.FONTS)

    # Inject the theme CSS
    if hasattr(theme_module, "CSS"):
        inject_css(theme_module.CSS)


def list_themes() -> list:
    """
    Get a list of all available theme names.
    
    Returns:
        List of theme name strings
        
    Example:
        themes = list_themes()
        print(themes)  # ['cosmic_purple', 'neon_tokyo', ...]
    """
    return list(AVAILABLE_THEMES.keys())


def get_theme_info(theme_name: str) -> dict:
    """
    Get information about a specific theme.
    
    Args:
        theme_name: Name of the theme
        
    Returns:
        Dictionary with theme metadata
    """
    if theme_name not in AVAILABLE_THEMES:
        return None

    import importlib
    theme_module = importlib.import_module(AVAILABLE_THEMES[theme_name])

    return {
        "name": theme_name,
        "description": getattr(theme_module, "DESCRIPTION", ""),
        "colors": getattr(theme_module, "COLORS", {}),
        "fonts": getattr(theme_module, "FONTS", []),
    }
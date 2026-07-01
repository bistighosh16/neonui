"""
Neon Tokyo Theme 🕹️🌃
Cyberpunk arcade vibes - Akihabara at night!
Electric purple, neon cyan, hot pink with CRT scanlines and pixel fonts.
"""

DESCRIPTION = "Cyberpunk arcade vibes with CRT scanlines, pixel fonts, and electric neon glows 🕹️🌃"

COLORS = {
    "bg_primary": "#0a0011",
    "bg_surface": "#110022",
    "bg_card": "#1a0033",
    "primary": "#BF00FF",
    "accent_cyan": "#00FFFF",
    "accent_pink": "#FF006E",
    "accent_yellow": "#FFE600",
    "accent_green": "#39FF14",
    "text_primary": "#E0D0FF",
    "text_muted": "#9980CC",
    "border_glow": "rgba(191, 0, 255, 0.4)",
}

FONTS = [
    ("Press Start 2P", None),
    ("Orbitron", [400, 700, 900]),
    ("Share Tech Mono", None),
]

CSS = """
/* ═══════════════════════════════════════════
   NEON TOKYO THEME 🕹️🌃
═══════════════════════════════════════════ */

:root {
    --nt-bg-primary: #0a0011;
    --nt-bg-surface: #110022;
    --nt-bg-card: #1a0033;
    --nt-primary: #BF00FF;
    --nt-cyan: #00FFFF;
    --nt-pink: #FF006E;
    --nt-yellow: #FFE600;
    --nt-green: #39FF14;
    --nt-text-primary: #E0D0FF;
    --nt-text-muted: #9980CC;
    --nt-border-glow: rgba(191, 0, 255, 0.4);
}

* { box-sizing: border-box; }

.stApp {
    background-color: var(--nt-bg-primary) !important;
    background-image:
        radial-gradient(ellipse at 20% 50%, rgba(191,0,255,0.08) 0%, transparent 50%),
        radial-gradient(ellipse at 80% 20%, rgba(0,255,255,0.06) 0%, transparent 50%),
        radial-gradient(ellipse at 50% 80%, rgba(255,0,110,0.05) 0%, transparent 50%);
    min-height: 100vh;
    font-family: 'Share Tech Mono', monospace;
    color: var(--nt-text-primary);
}

/* ─── CRT SCANLINE OVERLAY ─── */
.stApp::before {
    content: '';
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background: repeating-linear-gradient(
        0deg,
        transparent,
        transparent 2px,
        rgba(0,0,0,0.04) 2px,
        rgba(0,0,0,0.04) 4px
    );
    pointer-events: none;
    z-index: 9999;
}

.block-container {
    padding: 2rem 3rem !important;
    max-width: 1200px !important;
    position: relative;
    z-index: 1;
}

#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
.stDeployButton { display: none !important; }

/* Keep header but hide its default background */
header[data-testid="stHeader"] {
    background: transparent !important;
    height: auto !important;
}

/* Ensure the sidebar toggle button stays visible and styled! */
button[data-testid="stSidebarCollapsedControl"],
button[kind="header"] {
    visibility: visible !important;
    display: flex !important;
    color: inherit !important;
    opacity: 0.7 !important;
    transition: opacity 0.3s ease !important;
}

button[data-testid="stSidebarCollapsedControl"]:hover,
button[kind="header"]:hover {
    opacity: 1 !important;
}

::-webkit-scrollbar { width: 8px; }
::-webkit-scrollbar-track { background: var(--nt-bg-primary); }
::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, var(--nt-primary), var(--nt-cyan));
    border-radius: 4px;
}

/* ─── TYPOGRAPHY ─── */
h1, h2, h3, h4, h5, h6 {
    font-family: 'Orbitron', sans-serif !important;
    color: var(--nt-text-primary) !important;
    font-weight: 900 !important;
    letter-spacing: 2px !important;
    text-transform: uppercase;
}

h1 {
    font-family: 'Press Start 2P', cursive !important;
    font-size: 2rem !important;
    background: linear-gradient(135deg, #BF00FF, #00FFFF, #FF006E);
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    background-clip: text !important;
    filter: drop-shadow(0 0 20px rgba(191,0,255,0.7));
    line-height: 1.5 !important;
}

h2 {
    color: var(--nt-primary) !important;
    text-shadow: 0 0 15px rgba(191,0,255,0.7);
    font-size: 1.5rem !important;
}

h3 {
    color: var(--nt-cyan) !important;
    text-shadow: 0 0 10px rgba(0,255,255,0.5);
    font-size: 1.2rem !important;
}

p, span, div, li {
    color: var(--nt-text-primary);
    font-family: 'Share Tech Mono', monospace;
}

code {
    background: var(--nt-bg-card) !important;
    color: var(--nt-cyan) !important;
    padding: 2px 8px !important;
    border-radius: 4px !important;
    font-family: 'Share Tech Mono', monospace !important;
    border: 1px solid var(--nt-border-glow);
}

/* ─── INPUTS ─── */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stNumberInput > div > div > input {
    background: rgba(17, 0, 34, 0.9) !important;
    border: 1px solid var(--nt-border-glow) !important;
    border-radius: 8px !important;
    color: var(--nt-text-primary) !important;
    font-family: 'Share Tech Mono', monospace !important;
    font-size: 0.95rem !important;
}

.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: var(--nt-cyan) !important;
    box-shadow: 0 0 20px rgba(0,255,255,0.4) !important;
}

.stSelectbox > div > div {
    background: rgba(17, 0, 34, 0.9) !important;
    border: 1px solid var(--nt-border-glow) !important;
    border-radius: 8px !important;
    color: var(--nt-text-primary) !important;
}

/* ─── BUTTONS ─── */
.stButton > button {
    background: linear-gradient(135deg, rgba(191,0,255,0.2), rgba(0,255,255,0.1)) !important;
    border: 1px solid var(--nt-primary) !important;
    color: var(--nt-text-primary) !important;
    font-family: 'Orbitron', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.85rem !important;
    letter-spacing: 2px !important;
    border-radius: 8px !important;
    text-transform: uppercase !important;
    padding: 0.6rem 1.5rem !important;
    transition: all 0.3s ease !important;
}

.stButton > button:hover {
    background: linear-gradient(135deg, rgba(191,0,255,0.4), rgba(0,255,255,0.2)) !important;
    border-color: var(--nt-cyan) !important;
    box-shadow: 0 0 25px rgba(0,255,255,0.5) !important;
    transform: translateY(-2px) !important;
}

.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, var(--nt-primary), var(--nt-cyan)) !important;
    border: none !important;
    color: #0a0011 !important;
    font-weight: 900 !important;
    box-shadow: 0 0 20px rgba(191,0,255,0.6) !important;
}

.stButton > button[kind="primary"]:hover {
    box-shadow: 0 0 35px rgba(191,0,255,0.9) !important;
}

/* ─── METRICS ─── */
[data-testid="stMetric"] {
    background: rgba(17, 0, 34, 0.9) !important;
    border: 2px solid var(--nt-primary) !important;
    border-radius: 12px !important;
    padding: 1.2rem !important;
    box-shadow: 0 0 20px rgba(191,0,255,0.2);
}

[data-testid="stMetricLabel"] {
    color: var(--nt-cyan) !important;
    font-family: 'Orbitron', sans-serif !important;
    letter-spacing: 2px !important;
    text-transform: uppercase;
    font-size: 0.75rem !important;
}

[data-testid="stMetricValue"] {
    color: var(--nt-yellow) !important;
    font-family: 'Press Start 2P', cursive !important;
    text-shadow: 0 0 15px rgba(255,230,0,0.6);
    font-size: 1.5rem !important;
}

/* ─── TABS ─── */
.stTabs [data-baseweb="tab"] {
    background: rgba(17, 0, 34, 0.5) !important;
    color: var(--nt-text-muted) !important;
    border-radius: 8px 8px 0 0 !important;
    font-family: 'Orbitron', sans-serif !important;
    text-transform: uppercase !important;
    letter-spacing: 2px !important;
}

.stTabs [aria-selected="true"] {
    color: var(--nt-cyan) !important;
    background: linear-gradient(135deg, rgba(191,0,255,0.3), rgba(0,255,255,0.2)) !important;
    text-shadow: 0 0 10px rgba(0,255,255,0.5);
}

/* ─── ALERTS ─── */
.stAlert {
    background: rgba(17, 0, 34, 0.9) !important;
    border: 1px solid var(--nt-border-glow) !important;
    border-radius: 8px !important;
    color: var(--nt-text-primary) !important;
    font-family: 'Share Tech Mono', monospace !important;
}

.stSuccess { border-left: 4px solid var(--nt-green) !important; }
.stError { border-left: 4px solid var(--nt-pink) !important; }
.stWarning { border-left: 4px solid var(--nt-yellow) !important; }
.stInfo { border-left: 4px solid var(--nt-cyan) !important; }

/* ─── SPINNER ─── */
.stSpinner > div {
    border-top-color: var(--nt-primary) !important;
    border-right-color: var(--nt-cyan) !important;
}

/* ─── DIVIDER ─── */
hr {
    border: none !important;
    height: 1px !important;
    background: linear-gradient(90deg, transparent, var(--nt-primary), var(--nt-cyan), transparent) !important;
}

/* ─── LABELS ─── */
.stTextInput label,
.stTextArea label,
.stSelectbox label,
.stRadio label span,
.stNumberInput label,
.stSlider label {
    color: var(--nt-cyan) !important;
    font-family: 'Orbitron', sans-serif !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    font-size: 0.75rem !important;
}

/* ─── SLIDER ─── */
.stSlider [data-baseweb="slider"] > div > div > div {
    background: linear-gradient(90deg, var(--nt-primary), var(--nt-cyan)) !important;
}

.stSlider [role="slider"] {
    background: var(--nt-yellow) !important;
    border: 2px solid var(--nt-primary) !important;
    box-shadow: 0 0 15px rgba(255,230,0,0.6) !important;
}

/* ─── EXPANDER ─── */
.streamlit-expanderHeader,
[data-testid="stExpander"] summary {
    background: rgba(17, 0, 34, 0.8) !important;
    border: 1px solid var(--nt-border-glow) !important;
    border-radius: 8px !important;
    color: var(--nt-cyan) !important;
    font-family: 'Orbitron', sans-serif !important;
    text-transform: uppercase !important;
    letter-spacing: 2px !important;
}

/* ─── SIDEBAR ─── */
section[data-testid="stSidebar"] {
    background: rgba(10, 0, 17, 0.98) !important;
    border-right: 1px solid var(--nt-border-glow) !important;
}
"""
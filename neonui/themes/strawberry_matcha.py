"""
Strawberry Matcha Theme 🍓🍵
Cute cottagecore vibes - soft sage green matcha with strawberry pink accents.
Cozy, warm, and absolutely adorable!
"""

DESCRIPTION = "Cute cottagecore vibes with soft sage matcha green and strawberry pink accents 🍓🍵"

COLORS = {
    "bg_primary": "#FAF7F2",
    "bg_surface": "#F4EFE6",
    "bg_card": "#FFFFFF",
    "matcha": "#87A96B",
    "matcha_dark": "#6B8E4E",
    "matcha_light": "#A8C88A",
    "strawberry": "#FF9AA2",
    "strawberry_dark": "#E77582",
    "strawberry_light": "#FFC5CA",
    "cream": "#FFF5E4",
    "text_primary": "#3D3D3D",
    "text_muted": "#6B6B6B",
    "text_dim": "#999999",
    "border": "rgba(135, 169, 107, 0.3)",
}

FONTS = [
    ("Fredoka", [400, 500, 600, 700]),
    ("Quicksand", [400, 500, 600, 700]),
]

CSS = """
/* ═══════════════════════════════════════════
   STRAWBERRY MATCHA THEME 🍓🍵
═══════════════════════════════════════════ */

:root {
    --sm-bg-primary: #FAF7F2;
    --sm-bg-surface: #F4EFE6;
    --sm-bg-card: #FFFFFF;
    --sm-matcha: #87A96B;
    --sm-matcha-dark: #6B8E4E;
    --sm-matcha-light: #A8C88A;
    --sm-strawberry: #FF9AA2;
    --sm-strawberry-dark: #E77582;
    --sm-strawberry-light: #FFC5CA;
    --sm-cream: #FFF5E4;
    --sm-text-primary: #3D3D3D;
    --sm-text-muted: #6B6B6B;
    --sm-text-dim: #999999;
    --sm-border: rgba(135, 169, 107, 0.3);
    --sm-shadow: rgba(135, 169, 107, 0.15);
}

* { box-sizing: border-box; }

.stApp {
    background-color: var(--sm-bg-primary) !important;
    background-image:
        radial-gradient(circle at 20% 30%, rgba(255, 154, 162, 0.08) 0%, transparent 40%),
        radial-gradient(circle at 80% 70%, rgba(135, 169, 107, 0.1) 0%, transparent 40%),
        radial-gradient(circle at 50% 90%, rgba(255, 197, 202, 0.08) 0%, transparent 40%);
    min-height: 100vh;
    font-family: 'Quicksand', sans-serif;
    color: var(--sm-text-primary);
}

.block-container {
    padding: 2rem 3rem !important;
    max-width: 1200px !important;
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

::-webkit-scrollbar { width: 10px; }
::-webkit-scrollbar-track { background: var(--sm-bg-surface); }
::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, var(--sm-matcha), var(--sm-strawberry));
    border-radius: 5px;
}

/* ─── TYPOGRAPHY ─── */
h1, h2, h3, h4, h5, h6 {
    font-family: 'Fredoka', 'Quicksand', sans-serif !important;
    color: var(--sm-text-primary) !important;
    font-weight: 700 !important;
}

h1 {
    font-size: 2.5rem !important;
    background: linear-gradient(135deg, var(--sm-matcha), var(--sm-strawberry));
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    background-clip: text !important;
}

h2 {
    color: var(--sm-matcha-dark) !important;
    font-size: 1.8rem !important;
}

h3 {
    color: var(--sm-strawberry-dark) !important;
    font-size: 1.4rem !important;
}

p, span, div, li {
    color: var(--sm-text-primary);
    font-family: 'Quicksand', sans-serif;
    line-height: 1.7;
}

code {
    background: var(--sm-cream) !important;
    color: var(--sm-strawberry-dark) !important;
    padding: 2px 8px !important;
    border-radius: 8px !important;
    font-family: 'Courier New', monospace !important;
    border: 1px solid var(--sm-border);
}

/* ─── INPUTS ─── */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stNumberInput > div > div > input {
    background: var(--sm-bg-card) !important;
    border: 2px solid var(--sm-border) !important;
    border-radius: 16px !important;
    color: var(--sm-text-primary) !important;
    font-family: 'Quicksand', sans-serif !important;
    padding: 0.7rem 1rem !important;
    box-shadow: 0 2px 8px var(--sm-shadow);
}

.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: var(--sm-matcha) !important;
    box-shadow: 0 0 0 4px rgba(135, 169, 107, 0.15) !important;
}

.stSelectbox > div > div {
    background: var(--sm-bg-card) !important;
    border: 2px solid var(--sm-border) !important;
    border-radius: 16px !important;
    color: var(--sm-text-primary) !important;
}

/* ─── BUTTONS ─── */
.stButton > button {
    background: var(--sm-bg-card) !important;
    border: 2px solid var(--sm-matcha) !important;
    color: var(--sm-matcha-dark) !important;
    font-family: 'Fredoka', sans-serif !important;
    font-weight: 600 !important;
    border-radius: 25px !important;
    padding: 0.6rem 1.5rem !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 2px 8px var(--sm-shadow);
}

.stButton > button:hover {
    background: var(--sm-matcha) !important;
    color: white !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 4px 15px rgba(135, 169, 107, 0.4) !important;
}

.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, var(--sm-strawberry), var(--sm-strawberry-dark)) !important;
    border: none !important;
    color: white !important;
    font-weight: 700 !important;
    box-shadow: 0 4px 15px rgba(231, 117, 130, 0.3) !important;
}

.stButton > button[kind="primary"]:hover {
    background: linear-gradient(135deg, var(--sm-strawberry-dark), var(--sm-strawberry)) !important;
    box-shadow: 0 6px 20px rgba(231, 117, 130, 0.5) !important;
    transform: translateY(-3px) !important;
}

/* ─── METRICS ─── */
[data-testid="stMetric"] {
    background: var(--sm-bg-card) !important;
    border: 2px solid var(--sm-border) !important;
    border-radius: 20px !important;
    padding: 1.2rem !important;
    box-shadow: 0 4px 20px var(--sm-shadow);
    transition: all 0.3s ease;
}

[data-testid="stMetric"]:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 25px rgba(135, 169, 107, 0.25) !important;
    border-color: var(--sm-matcha) !important;
}

[data-testid="stMetricLabel"] {
    color: var(--sm-text-muted) !important;
    font-family: 'Fredoka', sans-serif !important;
    font-weight: 500 !important;
}

[data-testid="stMetricValue"] {
    color: var(--sm-matcha-dark) !important;
    font-family: 'Fredoka', sans-serif !important;
    font-weight: 700 !important;
}

/* ─── TABS ─── */
.stTabs [data-baseweb="tab"] {
    background: var(--sm-bg-card) !important;
    color: var(--sm-text-muted) !important;
    border-radius: 16px 16px 0 0 !important;
    font-family: 'Fredoka', sans-serif !important;
    font-weight: 600 !important;
}

.stTabs [aria-selected="true"] {
    color: var(--sm-strawberry-dark) !important;
    background: var(--sm-strawberry-light) !important;
}

/* ─── ALERTS ─── */
.stAlert {
    background: var(--sm-bg-card) !important;
    border: 2px solid var(--sm-border) !important;
    border-radius: 16px !important;
    color: var(--sm-text-primary) !important;
    font-family: 'Quicksand', sans-serif !important;
    box-shadow: 0 2px 10px var(--sm-shadow);
}

.stSuccess { border-left: 4px solid var(--sm-matcha) !important; }
.stError { border-left: 4px solid var(--sm-strawberry-dark) !important; }
.stWarning { border-left: 4px solid #FFB84D !important; }
.stInfo { border-left: 4px solid #7EC8E3 !important; }

/* ─── SPINNER ─── */
.stSpinner > div {
    border-top-color: var(--sm-matcha) !important;
    border-right-color: var(--sm-strawberry) !important;
}

/* ─── DIVIDER ─── */
hr {
    border: none !important;
    height: 2px !important;
    background: linear-gradient(90deg, transparent, var(--sm-matcha-light), var(--sm-strawberry-light), transparent) !important;
    border-radius: 2px;
}

/* ─── LABELS ─── */
.stTextInput label,
.stTextArea label,
.stSelectbox label,
.stRadio label span,
.stNumberInput label,
.stSlider label {
    color: var(--sm-text-muted) !important;
    font-family: 'Fredoka', sans-serif !important;
    font-weight: 500 !important;
}

/* ─── SLIDER ─── */
.stSlider [data-baseweb="slider"] > div > div > div {
    background: linear-gradient(90deg, var(--sm-matcha), var(--sm-strawberry)) !important;
}

.stSlider [role="slider"] {
    background: white !important;
    border: 3px solid var(--sm-matcha) !important;
    box-shadow: 0 2px 8px var(--sm-shadow) !important;
}

/* ─── EXPANDER ─── */
.streamlit-expanderHeader,
[data-testid="stExpander"] summary {
    background: var(--sm-bg-card) !important;
    border: 2px solid var(--sm-border) !important;
    border-radius: 16px !important;
    color: var(--sm-matcha-dark) !important;
    font-family: 'Fredoka', sans-serif !important;
    font-weight: 600 !important;
    box-shadow: 0 2px 8px var(--sm-shadow);
}

/* ─── SIDEBAR ─── */
section[data-testid="stSidebar"] {
    background: var(--sm-bg-surface) !important;
    border-right: 2px solid var(--sm-border) !important;
}

/* ─── FILE UPLOADER ─── */
[data-testid="stFileUploader"] {
    background: var(--sm-bg-card) !important;
    border: 2px dashed var(--sm-matcha-light) !important;
    border-radius: 20px !important;
    box-shadow: 0 2px 10px var(--sm-shadow);
}
"""
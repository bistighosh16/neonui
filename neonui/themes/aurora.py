"""
Aurora Theme 🌈✨
Northern Lights vibes - flowing rainbow gradients with dreamy dark blue backgrounds.
Cyan, purple, pink, green - the sky is dancing!
"""

DESCRIPTION = "Northern Lights vibes with flowing rainbow gradients on dreamy dark blue 🌈✨"

COLORS = {
    "bg_primary": "#0B1929",
    "bg_surface": "#132844",
    "bg_card": "#1B3A5F",
    "aurora_cyan": "#00E5FF",
    "aurora_purple": "#B39DDB",
    "aurora_pink": "#F48FB1",
    "aurora_green": "#69F0AE",
    "aurora_teal": "#26C6DA",
    "text_primary": "#E3F2FD",
    "text_muted": "#90CAF9",
    "text_dim": "#5C7A99",
    "border_glow": "rgba(0, 229, 255, 0.3)",
}

FONTS = [
    ("Poppins", [400, 500, 600, 700]),
    ("Playfair Display", [400, 700, 900]),
]

CSS = """
/* ═══════════════════════════════════════════
   AURORA THEME 🌈✨
═══════════════════════════════════════════ */

:root {
    --au-bg-primary: #0B1929;
    --au-bg-surface: #132844;
    --au-bg-card: #1B3A5F;
    --au-cyan: #00E5FF;
    --au-purple: #B39DDB;
    --au-pink: #F48FB1;
    --au-green: #69F0AE;
    --au-teal: #26C6DA;
    --au-text-primary: #E3F2FD;
    --au-text-muted: #90CAF9;
    --au-text-dim: #5C7A99;
    --au-border-glow: rgba(0, 229, 255, 0.3);
}

* { box-sizing: border-box; }

@keyframes aurora-flow {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
}

.stApp {
    background-color: var(--au-bg-primary) !important;
    background-image:
        radial-gradient(ellipse at 10% 20%, rgba(0, 229, 255, 0.1) 0%, transparent 50%),
        radial-gradient(ellipse at 90% 40%, rgba(179, 157, 219, 0.12) 0%, transparent 50%),
        radial-gradient(ellipse at 50% 80%, rgba(244, 143, 177, 0.08) 0%, transparent 50%),
        radial-gradient(ellipse at 30% 90%, rgba(105, 240, 174, 0.06) 0%, transparent 50%);
    min-height: 100vh;
    font-family: 'Poppins', sans-serif;
    color: var(--au-text-primary);
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

::-webkit-scrollbar { width: 10px; }
::-webkit-scrollbar-track { background: var(--au-bg-primary); }
::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, var(--au-cyan), var(--au-purple), var(--au-pink));
    border-radius: 5px;
}

/* ─── TYPOGRAPHY ─── */
h1, h2, h3, h4, h5, h6 {
    font-family: 'Playfair Display', serif !important;
    color: var(--au-text-primary) !important;
    font-weight: 700 !important;
}

h1 {
    font-size: 2.8rem !important;
    background: linear-gradient(90deg, var(--au-cyan), var(--au-purple), var(--au-pink), var(--au-green), var(--au-cyan));
    background-size: 200% auto;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    background-clip: text !important;
    animation: aurora-flow 8s ease-in-out infinite;
    filter: drop-shadow(0 0 20px rgba(0, 229, 255, 0.4));
}

h2 {
    color: var(--au-cyan) !important;
    text-shadow: 0 0 15px rgba(0, 229, 255, 0.4);
    font-size: 1.8rem !important;
}

h3 {
    color: var(--au-purple) !important;
    font-size: 1.4rem !important;
    font-family: 'Poppins', sans-serif !important;
    font-weight: 600 !important;
}

p, span, div, li {
    color: var(--au-text-primary);
    font-family: 'Poppins', sans-serif;
    line-height: 1.7;
}

code {
    background: var(--au-bg-card) !important;
    color: var(--au-cyan) !important;
    padding: 2px 8px !important;
    border-radius: 6px !important;
    font-family: 'Courier New', monospace !important;
    border: 1px solid var(--au-border-glow);
}

/* ─── INPUTS ─── */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stNumberInput > div > div > input {
    background: rgba(19, 40, 68, 0.7) !important;
    border: 1px solid var(--au-border-glow) !important;
    border-radius: 12px !important;
    color: var(--au-text-primary) !important;
    font-family: 'Poppins', sans-serif !important;
    padding: 0.7rem 1rem !important;
    backdrop-filter: blur(10px);
}

.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: var(--au-cyan) !important;
    box-shadow: 0 0 20px rgba(0, 229, 255, 0.3) !important;
    background: rgba(27, 58, 95, 0.8) !important;
}

.stSelectbox > div > div {
    background: rgba(19, 40, 68, 0.7) !important;
    border: 1px solid var(--au-border-glow) !important;
    border-radius: 12px !important;
    color: var(--au-text-primary) !important;
}

/* ─── BUTTONS ─── */
.stButton > button {
    background: linear-gradient(135deg, rgba(0, 229, 255, 0.15), rgba(179, 157, 219, 0.1)) !important;
    border: 1px solid var(--au-cyan) !important;
    color: var(--au-text-primary) !important;
    font-family: 'Poppins', sans-serif !important;
    font-weight: 600 !important;
    border-radius: 12px !important;
    padding: 0.7rem 1.5rem !important;
    transition: all 0.3s ease !important;
    backdrop-filter: blur(10px);
}

.stButton > button:hover {
    background: linear-gradient(135deg, rgba(0, 229, 255, 0.3), rgba(179, 157, 219, 0.2)) !important;
    border-color: var(--au-purple) !important;
    box-shadow: 0 0 25px rgba(0, 229, 255, 0.4) !important;
    transform: translateY(-2px) !important;
}

.stButton > button[kind="primary"] {
    background: linear-gradient(90deg, var(--au-cyan), var(--au-purple), var(--au-pink)) !important;
    background-size: 200% auto !important;
    border: none !important;
    color: white !important;
    font-weight: 700 !important;
    animation: aurora-flow 4s ease-in-out infinite;
    box-shadow: 0 4px 20px rgba(0, 229, 255, 0.4) !important;
}

.stButton > button[kind="primary"]:hover {
    box-shadow: 0 6px 30px rgba(0, 229, 255, 0.6) !important;
    transform: translateY(-3px) !important;
}

/* ─── METRICS ─── */
[data-testid="stMetric"] {
    background: rgba(19, 40, 68, 0.6) !important;
    border: 1px solid var(--au-border-glow) !important;
    border-radius: 16px !important;
    padding: 1.2rem !important;
    backdrop-filter: blur(10px);
    transition: all 0.3s ease;
}

[data-testid="stMetric"]:hover {
    border-color: var(--au-cyan) !important;
    box-shadow: 0 0 25px rgba(0, 229, 255, 0.3) !important;
    transform: translateY(-3px);
}

[data-testid="stMetricLabel"] {
    color: var(--au-text-muted) !important;
    font-family: 'Poppins', sans-serif !important;
}

[data-testid="stMetricValue"] {
    color: var(--au-cyan) !important;
    font-family: 'Playfair Display', serif !important;
    text-shadow: 0 0 15px rgba(0, 229, 255, 0.4);
}

/* ─── TABS ─── */
.stTabs [data-baseweb="tab"] {
    background: rgba(19, 40, 68, 0.4) !important;
    color: var(--au-text-muted) !important;
    border-radius: 12px 12px 0 0 !important;
    font-family: 'Poppins', sans-serif !important;
    font-weight: 600 !important;
}

.stTabs [aria-selected="true"] {
    color: var(--au-cyan) !important;
    background: linear-gradient(135deg, rgba(0, 229, 255, 0.2), rgba(179, 157, 219, 0.15)) !important;
    text-shadow: 0 0 10px rgba(0, 229, 255, 0.4);
}

/* ─── ALERTS ─── */
.stAlert {
    background: rgba(19, 40, 68, 0.8) !important;
    border: 1px solid var(--au-border-glow) !important;
    border-radius: 12px !important;
    color: var(--au-text-primary) !important;
    backdrop-filter: blur(10px);
}

.stSuccess { border-left: 4px solid var(--au-green) !important; }
.stError { border-left: 4px solid var(--au-pink) !important; }
.stWarning { border-left: 4px solid #FFB74D !important; }
.stInfo { border-left: 4px solid var(--au-cyan) !important; }

/* ─── SPINNER ─── */
.stSpinner > div {
    border-top-color: var(--au-cyan) !important;
    border-right-color: var(--au-purple) !important;
}

/* ─── DIVIDER ─── */
hr {
    border: none !important;
    height: 2px !important;
    background: linear-gradient(90deg, transparent, var(--au-cyan), var(--au-purple), var(--au-pink), transparent) !important;
}

/* ─── LABELS ─── */
.stTextInput label,
.stTextArea label,
.stSelectbox label,
.stRadio label span,
.stNumberInput label,
.stSlider label {
    color: var(--au-text-muted) !important;
    font-family: 'Poppins', sans-serif !important;
    font-weight: 500 !important;
}

/* ─── SLIDER ─── */
.stSlider [data-baseweb="slider"] > div > div > div {
    background: linear-gradient(90deg, var(--au-cyan), var(--au-purple), var(--au-pink)) !important;
}

.stSlider [role="slider"] {
    background: var(--au-text-primary) !important;
    border: 2px solid var(--au-cyan) !important;
    box-shadow: 0 0 15px rgba(0, 229, 255, 0.5) !important;
}

/* ─── EXPANDER ─── */
.streamlit-expanderHeader,
[data-testid="stExpander"] summary {
    background: rgba(19, 40, 68, 0.6) !important;
    border: 1px solid var(--au-border-glow) !important;
    border-radius: 12px !important;
    color: var(--au-cyan) !important;
    font-family: 'Poppins', sans-serif !important;
    font-weight: 600 !important;
}

/* ─── SIDEBAR ─── */
section[data-testid="stSidebar"] {
    background: rgba(11, 25, 41, 0.95) !important;
    border-right: 1px solid var(--au-border-glow) !important;
    backdrop-filter: blur(20px);
}
"""
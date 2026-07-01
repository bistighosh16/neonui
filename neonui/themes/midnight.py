"""
Midnight Theme 🌙✨
Elegant minimal dark theme - sophisticated blacks and grays with subtle silver accents.
For when you want dark mode that feels premium, not gamer.
"""

DESCRIPTION = "Elegant minimal dark theme with sophisticated blacks, grays, and silver accents 🌙✨"

COLORS = {
    "bg_primary": "#0A0A0F",
    "bg_surface": "#141419",
    "bg_card": "#1C1C24",
    "silver": "#C0C0C0",
    "silver_bright": "#E8E8E8",
    "gold_accent": "#D4AF37",
    "blue_accent": "#4A9EFF",
    "text_primary": "#F5F5F7",
    "text_muted": "#A0A0A8",
    "text_dim": "#6B6B75",
    "border": "rgba(192, 192, 192, 0.15)",
    "border_hover": "rgba(192, 192, 192, 0.4)",
}

FONTS = [
    ("Inter", [300, 400, 500, 600, 700]),
    ("Cormorant Garamond", [400, 500, 600, 700]),
]

CSS = """
/* ═══════════════════════════════════════════
   MIDNIGHT THEME 🌙✨
═══════════════════════════════════════════ */

:root {
    --mn-bg-primary: #0A0A0F;
    --mn-bg-surface: #141419;
    --mn-bg-card: #1C1C24;
    --mn-silver: #C0C0C0;
    --mn-silver-bright: #E8E8E8;
    --mn-gold: #D4AF37;
    --mn-blue: #4A9EFF;
    --mn-text-primary: #F5F5F7;
    --mn-text-muted: #A0A0A8;
    --mn-text-dim: #6B6B75;
    --mn-border: rgba(192, 192, 192, 0.15);
    --mn-border-hover: rgba(192, 192, 192, 0.4);
}

* { box-sizing: border-box; }

.stApp {
    background-color: var(--mn-bg-primary) !important;
    background-image:
        radial-gradient(ellipse at 20% 30%, rgba(74, 158, 255, 0.03) 0%, transparent 60%),
        radial-gradient(ellipse at 80% 70%, rgba(212, 175, 55, 0.02) 0%, transparent 60%);
    min-height: 100vh;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    color: var(--mn-text-primary);
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

::-webkit-scrollbar { width: 8px; }
::-webkit-scrollbar-track { background: var(--mn-bg-primary); }
::-webkit-scrollbar-thumb {
    background: var(--mn-border-hover);
    border-radius: 4px;
}

/* ─── TYPOGRAPHY ─── */
h1, h2, h3, h4, h5, h6 {
    color: var(--mn-text-primary) !important;
    font-weight: 600 !important;
    letter-spacing: -0.02em;
}

h1 {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 3rem !important;
    font-weight: 500 !important;
    color: var(--mn-silver-bright) !important;
    letter-spacing: -0.03em;
    font-style: italic;
}

h2 {
    font-family: 'Inter', sans-serif !important;
    color: var(--mn-silver) !important;
    font-size: 1.8rem !important;
    font-weight: 500 !important;
}

h3 {
    font-family: 'Inter', sans-serif !important;
    color: var(--mn-text-primary) !important;
    font-size: 1.3rem !important;
    font-weight: 500 !important;
}

p, span, div, li {
    color: var(--mn-text-primary);
    font-family: 'Inter', sans-serif;
    line-height: 1.7;
    font-weight: 400;
}

code {
    background: var(--mn-bg-card) !important;
    color: var(--mn-blue) !important;
    padding: 2px 8px !important;
    border-radius: 4px !important;
    font-family: 'JetBrains Mono', monospace !important;
    border: 1px solid var(--mn-border);
}

/* ─── INPUTS ─── */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stNumberInput > div > div > input {
    background: var(--mn-bg-card) !important;
    border: 1px solid var(--mn-border) !important;
    border-radius: 8px !important;
    color: var(--mn-text-primary) !important;
    font-family: 'Inter', sans-serif !important;
    padding: 0.7rem 1rem !important;
    transition: all 0.2s ease !important;
}

.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: var(--mn-silver) !important;
    box-shadow: 0 0 0 3px rgba(192, 192, 192, 0.1) !important;
}

.stSelectbox > div > div {
    background: var(--mn-bg-card) !important;
    border: 1px solid var(--mn-border) !important;
    border-radius: 8px !important;
    color: var(--mn-text-primary) !important;
}

/* ─── BUTTONS ─── */
.stButton > button {
    background: transparent !important;
    border: 1px solid var(--mn-border-hover) !important;
    color: var(--mn-text-primary) !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 500 !important;
    font-size: 0.9rem !important;
    border-radius: 8px !important;
    padding: 0.6rem 1.5rem !important;
    transition: all 0.2s ease !important;
    letter-spacing: 0.02em;
}

.stButton > button:hover {
    background: var(--mn-bg-card) !important;
    border-color: var(--mn-silver) !important;
    color: var(--mn-silver-bright) !important;
    transform: translateY(-1px) !important;
}

.stButton > button[kind="primary"] {
    background: var(--mn-silver-bright) !important;
    color: var(--mn-bg-primary) !important;
    border: none !important;
    font-weight: 600 !important;
}

.stButton > button[kind="primary"]:hover {
    background: white !important;
    box-shadow: 0 4px 20px rgba(255, 255, 255, 0.15) !important;
    transform: translateY(-2px) !important;
}

/* ─── METRICS ─── */
[data-testid="stMetric"] {
    background: var(--mn-bg-card) !important;
    border: 1px solid var(--mn-border) !important;
    border-radius: 12px !important;
    padding: 1.2rem !important;
    transition: all 0.2s ease;
}

[data-testid="stMetric"]:hover {
    border-color: var(--mn-border-hover) !important;
    transform: translateY(-2px);
}

[data-testid="stMetricLabel"] {
    color: var(--mn-text-muted) !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 400 !important;
    font-size: 0.85rem !important;
    text-transform: uppercase;
    letter-spacing: 0.1em;
}

[data-testid="stMetricValue"] {
    color: var(--mn-silver-bright) !important;
    font-family: 'Cormorant Garamond', serif !important;
    font-weight: 500 !important;
}

/* ─── TABS ─── */
.stTabs [data-baseweb="tab-list"] {
    border-bottom: 1px solid var(--mn-border) !important;
}

.stTabs [data-baseweb="tab"] {
    background: transparent !important;
    color: var(--mn-text-muted) !important;
    border-radius: 0 !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 500 !important;
}

.stTabs [aria-selected="true"] {
    color: var(--mn-silver-bright) !important;
    background: transparent !important;
    border-bottom: 2px solid var(--mn-silver) !important;
}

/* ─── ALERTS ─── */
.stAlert {
    background: var(--mn-bg-card) !important;
    border: 1px solid var(--mn-border) !important;
    border-radius: 8px !important;
    color: var(--mn-text-primary) !important;
    font-family: 'Inter', sans-serif !important;
}

.stSuccess { border-left: 3px solid #4ADE80 !important; }
.stError { border-left: 3px solid #F87171 !important; }
.stWarning { border-left: 3px solid var(--mn-gold) !important; }
.stInfo { border-left: 3px solid var(--mn-blue) !important; }

/* ─── SPINNER ─── */
.stSpinner > div {
    border-top-color: var(--mn-silver) !important;
}

/* ─── DIVIDER ─── */
hr {
    border: none !important;
    height: 1px !important;
    background: var(--mn-border) !important;
    margin: 2rem 0 !important;
}

/* ─── LABELS ─── */
.stTextInput label,
.stTextArea label,
.stSelectbox label,
.stRadio label span,
.stNumberInput label,
.stSlider label {
    color: var(--mn-text-muted) !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 500 !important;
    font-size: 0.85rem !important;
    text-transform: uppercase;
    letter-spacing: 0.08em;
}

/* ─── SLIDER ─── */
.stSlider [data-baseweb="slider"] > div > div > div {
    background: var(--mn-silver) !important;
}

.stSlider [role="slider"] {
    background: var(--mn-silver-bright) !important;
    border: 2px solid var(--mn-bg-primary) !important;
}

/* ─── EXPANDER ─── */
.streamlit-expanderHeader,
[data-testid="stExpander"] summary {
    background: var(--mn-bg-card) !important;
    border: 1px solid var(--mn-border) !important;
    border-radius: 8px !important;
    color: var(--mn-text-primary) !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 500 !important;
}

/* ─── SIDEBAR ─── */
section[data-testid="stSidebar"] {
    background: var(--mn-bg-surface) !important;
    border-right: 1px solid var(--mn-border) !important;
}
"""
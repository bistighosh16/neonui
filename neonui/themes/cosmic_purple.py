"""
Cosmic Purple Theme 💜🌌
The signature Vivi aesthetic - deep space vibes with electric purple glows,
starry backgrounds, and glassmorphism magic.
"""

DESCRIPTION = "Deep cosmic vibes with electric purple, starry backgrounds, and glassmorphism magic 💜🌌"

COLORS = {
    "bg_primary": "#0f0524",
    "bg_surface": "#1a0d3e",
    "bg_card": "#251654",
    "primary": "#B24BF3",
    "primary_light": "#D084FF",
    "primary_dark": "#7B2CBF",
    "accent": "#FF6EC7",
    "accent_alt": "#4CC9F0",
    "text_primary": "#F0E6FF",
    "text_muted": "#B8A9D9",
    "text_dim": "#8878A8",
    "success": "#7FFF9E",
    "warning": "#FFD166",
    "error": "#FF5C8A",
    "border_glow": "rgba(178, 75, 243, 0.4)",
}

FONTS = [
    ("Inter", [400, 500, 600, 700]),
    ("Space Grotesk", [400, 500, 600, 700]),
    ("JetBrains Mono", [400, 500]),
]

CSS = """
/* ═══════════════════════════════════════════
   COSMIC PURPLE THEME 💜🌌
═══════════════════════════════════════════ */

/* ─── ROOT VARIABLES ─── */
:root {
    --cp-bg-primary: #0f0524;
    --cp-bg-surface: #1a0d3e;
    --cp-bg-card: #251654;
    --cp-primary: #B24BF3;
    --cp-primary-light: #D084FF;
    --cp-primary-dark: #7B2CBF;
    --cp-accent: #FF6EC7;
    --cp-accent-alt: #4CC9F0;
    --cp-text-primary: #F0E6FF;
    --cp-text-muted: #B8A9D9;
    --cp-text-dim: #8878A8;
    --cp-success: #7FFF9E;
    --cp-warning: #FFD166;
    --cp-error: #FF5C8A;
    --cp-border-glow: rgba(178, 75, 243, 0.4);
    --cp-glow-purple: rgba(178, 75, 243, 0.6);
    --cp-glow-pink: rgba(255, 110, 199, 0.5);
}

/* ─── GLOBAL RESET ─── */
* { box-sizing: border-box; }

/* ─── MAIN APP BACKGROUND ─── */
.stApp {
    background-color: var(--cp-bg-primary) !important;
    background-image:
        radial-gradient(ellipse at 20% 30%, rgba(178, 75, 243, 0.15) 0%, transparent 50%),
        radial-gradient(ellipse at 80% 70%, rgba(255, 110, 199, 0.12) 0%, transparent 50%),
        radial-gradient(ellipse at 50% 90%, rgba(76, 201, 240, 0.08) 0%, transparent 50%),
        radial-gradient(circle at 10% 80%, rgba(178, 75, 243, 0.1) 0%, transparent 40%);
    min-height: 100vh;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    color: var(--cp-text-primary);
}

/* ─── STARRY BACKGROUND OVERLAY ─── */
.stApp::before {
    content: '';
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background-image:
        radial-gradient(1px 1px at 20% 30%, white, transparent),
        radial-gradient(1px 1px at 60% 70%, rgba(255,255,255,0.5), transparent),
        radial-gradient(2px 2px at 50% 50%, white, transparent),
        radial-gradient(1px 1px at 80% 10%, rgba(255,255,255,0.7), transparent),
        radial-gradient(1px 1px at 90% 60%, white, transparent),
        radial-gradient(1px 1px at 33% 88%, rgba(255,255,255,0.4), transparent),
        radial-gradient(2px 2px at 15% 15%, rgba(178, 75, 243, 0.6), transparent);
    background-size: 250px 250px, 200px 200px, 300px 300px, 350px 350px, 180px 180px, 220px 220px, 400px 400px;
    background-repeat: repeat;
    pointer-events: none;
    z-index: 0;
    opacity: 0.6;
}

/* ─── MAIN CONTAINER ─── */
.block-container {
    padding: 2rem 3rem !important;
    max-width: 1200px !important;
    position: relative;
    z-index: 1;
}

/* ─── HIDE STREAMLIT DEFAULTS ─── */
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

/* ─── SCROLLBAR ─── */
::-webkit-scrollbar { width: 10px; }
::-webkit-scrollbar-track { background: var(--cp-bg-primary); }
::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, var(--cp-primary), var(--cp-accent));
    border-radius: 5px;
}
::-webkit-scrollbar-thumb:hover {
    background: var(--cp-primary-light);
}

/* ═══════════════════════════════════════════
   TYPOGRAPHY
═══════════════════════════════════════════ */

h1, h2, h3, h4, h5, h6 {
    font-family: 'Space Grotesk', 'Inter', sans-serif !important;
    color: var(--cp-text-primary) !important;
    font-weight: 700 !important;
    letter-spacing: -0.02em;
}

h1 {
    font-size: 2.5rem !important;
    background: linear-gradient(135deg, var(--cp-primary-light), var(--cp-accent));
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    background-clip: text !important;
    filter: drop-shadow(0 0 20px var(--cp-glow-purple));
}

h2 {
    font-size: 1.8rem !important;
    color: var(--cp-primary-light) !important;
    text-shadow: 0 0 20px var(--cp-glow-purple);
}

h3 {
    font-size: 1.4rem !important;
    color: var(--cp-text-primary) !important;
}

p, span, div, li {
    color: var(--cp-text-primary);
    font-family: 'Inter', sans-serif;
    line-height: 1.7;
}

code {
    background: var(--cp-bg-card) !important;
    color: var(--cp-accent) !important;
    padding: 2px 8px !important;
    border-radius: 6px !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.9em !important;
    border: 1px solid var(--cp-border-glow);
}

pre {
    background: var(--cp-bg-surface) !important;
    border: 1px solid var(--cp-border-glow) !important;
    border-radius: 12px !important;
    padding: 1rem !important;
}

a {
    color: var(--cp-accent) !important;
    text-decoration: none !important;
    transition: all 0.3s ease;
}

a:hover {
    color: var(--cp-primary-light) !important;
    text-shadow: 0 0 8px var(--cp-glow-purple);
}

/* ═══════════════════════════════════════════
   STREAMLIT WIDGET OVERRIDES
═══════════════════════════════════════════ */

/* ─── TEXT INPUTS ─── */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stNumberInput > div > div > input {
    background: rgba(26, 13, 62, 0.6) !important;
    border: 1px solid var(--cp-border-glow) !important;
    border-radius: 12px !important;
    color: var(--cp-text-primary) !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.95rem !important;
    padding: 0.6rem 1rem !important;
    backdrop-filter: blur(10px);
    transition: all 0.3s ease !important;
}

.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus,
.stNumberInput > div > div > input:focus {
    border-color: var(--cp-primary) !important;
    box-shadow: 0 0 20px var(--cp-glow-purple) !important;
    background: rgba(37, 22, 84, 0.8) !important;
}

/* ─── SELECT BOX ─── */
.stSelectbox > div > div {
    background: rgba(26, 13, 62, 0.6) !important;
    border: 1px solid var(--cp-border-glow) !important;
    border-radius: 12px !important;
    color: var(--cp-text-primary) !important;
    backdrop-filter: blur(10px);
}

.stSelectbox > div > div:hover {
    border-color: var(--cp-primary) !important;
    box-shadow: 0 0 15px var(--cp-glow-purple) !important;
}

/* ─── BUTTONS ─── */
.stButton > button {
    background: linear-gradient(135deg, rgba(178, 75, 243, 0.2), rgba(255, 110, 199, 0.1)) !important;
    border: 1px solid var(--cp-primary) !important;
    color: var(--cp-text-primary) !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.95rem !important;
    letter-spacing: 0.02em !important;
    border-radius: 12px !important;
    padding: 0.6rem 1.5rem !important;
    transition: all 0.3s ease !important;
    backdrop-filter: blur(10px);
    box-shadow: 0 0 10px rgba(178, 75, 243, 0.2);
}

.stButton > button:hover {
    background: linear-gradient(135deg, rgba(178, 75, 243, 0.4), rgba(255, 110, 199, 0.2)) !important;
    border-color: var(--cp-primary-light) !important;
    box-shadow: 0 0 25px var(--cp-glow-purple) !important;
    transform: translateY(-2px) !important;
    color: #FFFFFF !important;
}

.stButton > button:active {
    transform: translateY(0) !important;
}

/* ─── PRIMARY BUTTON ─── */
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, var(--cp-primary), var(--cp-accent)) !important;
    border: none !important;
    color: #FFFFFF !important;
    font-weight: 700 !important;
    box-shadow: 0 4px 20px var(--cp-glow-purple) !important;
}

.stButton > button[kind="primary"]:hover {
    background: linear-gradient(135deg, var(--cp-primary-light), var(--cp-accent)) !important;
    box-shadow: 0 6px 30px var(--cp-glow-purple) !important;
    transform: translateY(-3px) !important;
}

/* ─── DOWNLOAD BUTTON ─── */
.stDownloadButton > button {
    background: linear-gradient(135deg, rgba(76, 201, 240, 0.2), rgba(178, 75, 243, 0.2)) !important;
    border: 1px solid var(--cp-accent-alt) !important;
    color: var(--cp-text-primary) !important;
    border-radius: 12px !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 600 !important;
}

.stDownloadButton > button:hover {
    box-shadow: 0 0 20px rgba(76, 201, 240, 0.4) !important;
    transform: translateY(-2px) !important;
}

/* ─── CHECKBOX / RADIO / TOGGLE ─── */
.stCheckbox > label,
.stRadio > label,
.stRadio label {
    color: var(--cp-text-primary) !important;
    font-family: 'Inter', sans-serif !important;
}

.stToggle > label {
    color: var(--cp-text-primary) !important;
    font-family: 'Inter', sans-serif !important;
}

/* ─── SLIDER ─── */
.stSlider [data-baseweb="slider"] > div > div > div {
    background: linear-gradient(90deg, var(--cp-primary), var(--cp-accent)) !important;
}

.stSlider [role="slider"] {
    background: var(--cp-primary-light) !important;
    border: 2px solid var(--cp-text-primary) !important;
    box-shadow: 0 0 15px var(--cp-glow-purple) !important;
}

/* ─── EXPANDER ─── */
.streamlit-expanderHeader,
[data-testid="stExpander"] summary {
    background: rgba(26, 13, 62, 0.6) !important;
    border: 1px solid var(--cp-border-glow) !important;
    border-radius: 12px !important;
    color: var(--cp-text-primary) !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 600 !important;
    transition: all 0.3s ease !important;
}

.streamlit-expanderHeader:hover,
[data-testid="stExpander"] summary:hover {
    border-color: var(--cp-primary) !important;
    box-shadow: 0 0 15px var(--cp-glow-purple) !important;
}

/* ─── METRIC ─── */
[data-testid="stMetric"] {
    background: rgba(26, 13, 62, 0.6) !important;
    border: 1px solid var(--cp-border-glow) !important;
    border-radius: 16px !important;
    padding: 1.2rem !important;
    backdrop-filter: blur(10px);
    transition: all 0.3s ease;
}

[data-testid="stMetric"]:hover {
    border-color: var(--cp-primary) !important;
    box-shadow: 0 0 25px var(--cp-glow-purple) !important;
    transform: translateY(-3px);
}

[data-testid="stMetricLabel"] {
    color: var(--cp-text-muted) !important;
    font-family: 'Inter', sans-serif !important;
}

[data-testid="stMetricValue"] {
    color: var(--cp-primary-light) !important;
    font-family: 'Space Grotesk', sans-serif !important;
    text-shadow: 0 0 15px var(--cp-glow-purple);
}

/* ─── TABS ─── */
.stTabs [data-baseweb="tab-list"] {
    background: transparent !important;
    border-bottom: 1px solid var(--cp-border-glow) !important;
    gap: 0.5rem;
}

.stTabs [data-baseweb="tab"] {
    background: rgba(26, 13, 62, 0.4) !important;
    color: var(--cp-text-muted) !important;
    border-radius: 12px 12px 0 0 !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 600 !important;
    padding: 0.6rem 1.2rem !important;
    transition: all 0.3s ease !important;
}

.stTabs [data-baseweb="tab"]:hover {
    color: var(--cp-text-primary) !important;
    background: rgba(178, 75, 243, 0.2) !important;
}

.stTabs [aria-selected="true"] {
    color: var(--cp-primary-light) !important;
    background: linear-gradient(135deg, rgba(178, 75, 243, 0.3), rgba(255, 110, 199, 0.2)) !important;
    text-shadow: 0 0 10px var(--cp-glow-purple);
}

/* ─── FILE UPLOADER ─── */
[data-testid="stFileUploader"] {
    background: rgba(26, 13, 62, 0.4) !important;
    border: 2px dashed var(--cp-border-glow) !important;
    border-radius: 16px !important;
    padding: 1.5rem !important;
    transition: all 0.3s ease !important;
}

[data-testid="stFileUploader"]:hover {
    border-color: var(--cp-primary) !important;
    background: rgba(26, 13, 62, 0.6) !important;
    box-shadow: 0 0 20px var(--cp-glow-purple) !important;
}

/* ─── ALERTS ─── */
.stAlert {
    background: rgba(26, 13, 62, 0.8) !important;
    border: 1px solid var(--cp-border-glow) !important;
    border-radius: 12px !important;
    color: var(--cp-text-primary) !important;
    backdrop-filter: blur(10px);
}

.stSuccess {
    border-left: 4px solid var(--cp-success) !important;
}

.stError {
    border-left: 4px solid var(--cp-error) !important;
}

.stWarning {
    border-left: 4px solid var(--cp-warning) !important;
}

.stInfo {
    border-left: 4px solid var(--cp-accent-alt) !important;
}

/* ─── SPINNER ─── */
.stSpinner > div {
    border-top-color: var(--cp-primary) !important;
    border-right-color: var(--cp-accent) !important;
}

/* ─── DIVIDER ─── */
hr {
    border: none !important;
    height: 1px !important;
    background: linear-gradient(90deg, transparent, var(--cp-primary), transparent) !important;
    margin: 2rem 0 !important;
}

/* ─── LABELS ─── */
.stTextInput label,
.stTextArea label,
.stSelectbox label,
.stRadio label span,
.stNumberInput label,
.stSlider label {
    color: var(--cp-text-muted) !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 500 !important;
    font-size: 0.9rem !important;
}

/* ─── SIDEBAR ─── */
section[data-testid="stSidebar"] {
    background: rgba(15, 5, 36, 0.95) !important;
    border-right: 1px solid var(--cp-border-glow) !important;
    backdrop-filter: blur(20px);
}

/* ─── DATAFRAMES ─── */
.stDataFrame {
    background: rgba(26, 13, 62, 0.6) !important;
    border: 1px solid var(--cp-border-glow) !important;
    border-radius: 12px !important;
}

/* ─── CODE BLOCKS ─── */
.stCodeBlock {
    background: var(--cp-bg-surface) !important;
    border: 1px solid var(--cp-border-glow) !important;
    border-radius: 12px !important;
}

/* ─── CAPTION ─── */
.stCaption {
    color: var(--cp-text-dim) !important;
    font-family: 'Inter', sans-serif !important;
}

/* ─── MARKDOWN LINKS ─── */
[data-testid="stMarkdownContainer"] a {
    color: var(--cp-accent) !important;
    text-decoration: none !important;
    border-bottom: 1px dashed var(--cp-accent);
    transition: all 0.3s ease;
}

[data-testid="stMarkdownContainer"] a:hover {
    color: var(--cp-primary-light) !important;
    border-bottom-color: var(--cp-primary-light);
    text-shadow: 0 0 8px var(--cp-glow-purple);
}
"""
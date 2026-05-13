import streamlit as st
from prompt import prompt
from parser import parser
from model import get_model
from config import (
    INTENT_CATEGORIES,
    URGENCY_LEVELS,
    TONE_TYPES,
    TEST_CASES
)
from langchain_core.exceptions import OutputParserException

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Email Intent & Urgency Detector",
    page_icon="📧",
    layout="wide"
)

# =========================================================
# SESSION STATE
# =========================================================

if "selected_test" not in st.session_state:
    st.session_state.selected_test = None

# =========================================================
# CUSTOM CSS
# =========================================================


st.markdown("""
<style>

/* =========================================================
   GLOBAL APP
========================================================= */

.stApp {
    background-color: #f4f7fb;
    color: #333333;
    font-family: 'Segoe UI', sans-serif;
}

/* =========================================================
   HEADERS
========================================================= */

h1, h2, h3, h4, h5 {
    color: #222222 !important;
}

/* =========================================================
   HEADER CONTAINER
========================================================= */

.header-container {
    padding: 2rem;
    text-align: center;
    background: linear-gradient(135deg, #667eea, #764ba2);
    border-radius: 20px;
    margin-bottom: 25px;
    color: white;
    box-shadow: 0 6px 18px rgba(0,0,0,0.1);
}

.header-container h1 {
    color: white !important;
    font-size: 3rem;
    text-shadow: 2px 2px 6px rgba(0,0,0,0.25);
}

.header-container p {
    color: #f0f0f0;
    font-size: 1.1rem;
}

/* =========================================================
   CARDS
========================================================= */

.card, .sidebar-card {
    background: #ffffff;
    padding: 25px;
    border-radius: 16px;
    border: 2px solid #667eea;
    margin-bottom: 20px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}

/* =========================================================
   METRIC BOXES
========================================================= */

.metric-box {
    background: linear-gradient(135deg, #667eea, #764ba2);
    padding: 20px;
    border-radius: 16px;
    text-align: center;
    color: red;
    box-shadow: 0 6px 15px rgba(102,126,234,0.3);
    transition: all 0.3s ease;
}

.metric-box:hover {
    transform: translateY(-5px);
}

.metric-label {
    font-size: 0.9rem;
    font-weight: 700;
    text-transform: uppercase;
    color: #ffffff;
    letter-spacing: 1px;
    text-shadow: 1px 1px 3px rgba(0,0,0,0.2);
}

.metric-value {
    font-size: 1.5rem;
    font-weight: bold;
    margin-top: 10px;
    color: #ffffff;
    text-shadow: 2px 2px 6px rgba(0,0,0,0.3);
}

/* =========================================================
   INPUT AREAS
========================================================= */

textarea {
    background-color: #ffffff !important;
    color: #333333 !important;
    border-radius: 12px !important;
    border: 2px solid #667eea !important;
    padding: 12px !important;
}

/* =========================================================
   SELECT BOX
========================================================= */

.stSelectbox div[data-baseweb="select"] {
    background-color: red !important;
    color: #333333 !important;
    border-radius: 10px !important;
    border: 2px solid #667eea !important;
}

/* =========================================================
   BUTTONS
========================================================= */

.stButton > button {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: orange;
    border: none;
    border-radius: 12px;
    padding: 0.75rem 1.2rem;
    font-weight: 700;
    transition: all 0.3s ease;
    box-shadow: 0 4px 10px rgba(102,126,234,0.3);
}

.stButton > button:hover {
    transform: scale(1.03);
    box-shadow: 0 6px 16px rgba(102,126,234,0.4);
}

/* =========================================================
   TABS
========================================================= */

.stTabs [data-baseweb="tab"] {
    background-color: #e9ecff;
    color: #333333;
    border-radius: 10px 10px 0 0;
    padding: 10px;
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, #667eea, #764ba2) !important;
    color:  #333333 !important;
}

/* =========================================================
   SUCCESS / ERROR / WARNING / INFO
========================================================= */

.stSuccess {
    background-color: #d4edda !important;
    color: #155724 !important;
    border-radius: 10px;
}

.stError {
    background-color: #f8d7da !important;
    color: #721c24 !important;
    border-radius: 10px;
}

.stWarning {
    background-color: #fff3cd !important;
    color: #856404 !important;
    border-radius: 10px;
}

.stInfo {
    background-color: #d1ecf1 !important;
    color: #0c5460 !important;
    border-radius: 10px;
}

/* =========================================================
   FOOTER
========================================================= */

.footer {
    text-align: center;
    padding: 20px;
    color: #555555;
    margin-top: 40px;
    border-top: 2px solid #cccccc;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class="header-container">
    <h1>📧 Email Intent & Urgency Detector</h1>
    <p>Analyze Email Intent, Urgency & Tone using AI</p>
</div>
""", unsafe_allow_html=True)

# =========================================================
# LAYOUT COLUMNS
# =========================================================

col1, col2 = st.columns([2, 1])

# =========================================================
# LEFT COLUMN
# =========================================================

with col1:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("✉️ Enter Email")

    email_input = st.text_area(
        "Paste your email here",
        height=250,
        placeholder="Type or paste an email..."
    )

    if st.button("🔍 Analyze Email", use_container_width=True):

        if email_input.strip():

            try:
                model, langfuse_handler = get_model()

                chain = prompt | model | parser

                result = chain.invoke(
                    {"text": email_input},
                    config={"callbacks": [langfuse_handler]}
                )

                st.success("✅ Analysis Complete")

                c1, c2, c3 = st.columns(3)

                with c1:
                    st.markdown(f"""
                    <div class="metric-box">
                        <div class="metric-label">Intent</div>
                        <div class="metric-value">{result.intent}</div>
                    </div>
                    """, unsafe_allow_html=True)

                with c2:
                    st.markdown(f"""
                    <div class="metric-box">
                        <div class="metric-label">Urgency</div>
                        <div class="metric-value">{result.urgency}</div>
                    </div>
                    """, unsafe_allow_html=True)

                with c3:
                    st.markdown(f"""
                    <div class="metric-box">
                        <div class="metric-label">Tone</div>
                        <div class="metric-value">{result.tone}</div>
                    </div>
                    """, unsafe_allow_html=True)

            except OutputParserException:
                st.error("❌ Failed to parse model output")

            except Exception as e:
                st.error(f"❌ Error: {e}")

        else:
            st.warning("⚠️ Please enter an email.")

    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# RIGHT COLUMN
# =========================================================

with col2:

    st.markdown('<div class="sidebar-card">', unsafe_allow_html=True)

    st.markdown("### 📋 Classification Guide")

    with st.expander("🎯 Intent Types", expanded=True):
        for intent, desc in INTENT_CATEGORIES.items():
            st.markdown(f"**{intent}**")
            st.write(desc)

    with st.expander("⚡ Urgency Levels", expanded=True):
        for urgency, desc in URGENCY_LEVELS.items():
            st.markdown(f"**{urgency}**")
            st.write(desc)

    with st.expander("🎭 Tone Types", expanded=True):
        for tone, desc in TONE_TYPES.items():
            st.markdown(f"**{tone}**")
            st.write(desc)

    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# TEST CASES
# =========================================================

st.divider()

st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("🧪 Test Cases")

tab1, tab2 = st.tabs([
    "📌 Select & Run",
    "📊 Batch Run All Tests"
])

# =========================================================
# TAB 1
# =========================================================

with tab1:

    selected_test = st.selectbox(
        "Choose Test Case",
        list(TEST_CASES.keys())
    )

    if st.button("▶️ Run Test", use_container_width=True):

        test_data = TEST_CASES[selected_test]

        st.markdown("### 📩 Email")
        st.info(test_data["email"])

        st.markdown("### ✅ Expected Output")

        st.write("Intent:", test_data["expected_intent"])
        st.write("Urgency:", test_data["expected_urgency"])
        st.write("Tone:", test_data["expected_tone"])

# =========================================================
# TAB 2
# =========================================================

with tab2:

    st.write("Run all test cases.")

    if st.button("🚀 Run All Tests", use_container_width=True):

        progress = st.progress(0)

        total = len(TEST_CASES)
        passed = 0

        for i, (name, data) in enumerate(TEST_CASES.items()):

            try:
                model, langfuse_handler = get_model()

                chain = prompt | model | parser

                result = chain.invoke(
                    {"text": data["email"]},
                    config={"callbacks": [langfuse_handler]}
                )

                ok = (
                    result.intent == data["expected_intent"]
                    and result.urgency == data["expected_urgency"]
                    and result.tone == data["expected_tone"]
                )

                if ok:
                    passed += 1
                    st.success(f"✅ {name} Passed")
                else:
                    st.error(f"❌ {name} Failed")

            except Exception as e:
                st.error(f"❌ {name}: {e}")

            progress.progress((i + 1) / total)

        st.success(f"🎉 Passed {passed}/{total} tests")

st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">
    <h4>🚀 Email Intent & Urgency Detector</h4>
    <p>Powered by LangChain + Groq + Pydantic</p>
    <p>Made with  by Ambika Ramireddy</p>
</div>
""", unsafe_allow_html=True)
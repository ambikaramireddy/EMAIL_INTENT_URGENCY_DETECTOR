import warnings
warnings.filterwarnings("ignore")
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
)

# =========================================================
# CACHE MODEL
# =========================================================

@st.cache_resource
def load_model():
    return get_model()

# =========================================================
# TITLE
# =========================================================

st.title("📧 Email Intent & Urgency Detector")

st.write(
    "Analyze email intent, urgency, and tone using AI."
)

# =========================================================
# EMAIL INPUT
# =========================================================

email_input = st.text_area(
    "Enter Email",
    height=200
)

# =========================================================
# ANALYZE BUTTON
# =========================================================

if st.button("Analyze Email"):

    if email_input.strip():

        try:

            model, langfuse_handler = load_model()

            chain = prompt | model | parser

            with st.spinner("Analyzing..."):

                result = chain.invoke(
                    {"text": email_input},
                    config={
                        "callbacks": [langfuse_handler],
                        "run_name": "Email Analysis"
                    }
                )

            st.success("Analysis Complete")

            st.subheader("Result")

            st.write(f"Intent: {result.intent}")
            st.write(f"Urgency: {result.urgency}")
            st.write(f"Tone: {result.tone}")

        except OutputParserException:
            st.error("Failed to parse model output")

        except Exception as e:
            st.error(f"Error: {e}")

    else:
        st.warning("Please enter an email.")

# =========================================================
# CLASSIFICATION GUIDE
# =========================================================

st.divider()

st.header(" Classification Guide")

with st.expander("Intent Types"):

    for intent, desc in INTENT_CATEGORIES.items():

        st.write(f"• {intent} → {desc}")

with st.expander("Urgency Levels"):

    for urgency, desc in URGENCY_LEVELS.items():

        st.write(f"• {urgency} → {desc}")

with st.expander("Tone Types"):

    for tone, desc in TONE_TYPES.items():

        st.write(f"• {tone} → {desc}")

# =========================================================
# TEST CASES
# =========================================================

st.divider()

st.header(" Test Cases")

selected_test = st.selectbox(
    "Choose Test Case",
    list(TEST_CASES.keys())
)

if st.button("Run Test"):

    data = TEST_CASES[selected_test]

    st.subheader("Email")

    st.info(data["email"])

    st.subheader("Expected Output")

    st.write(f"Intent: {data['expected_intent']}")
    st.write(f"Urgency: {data['expected_urgency']}")
    st.write(f"Tone: {data['expected_tone']}")

# =========================================================
# FOOTER
# =========================================================

st.divider()

st.write(" Built with Streamlit + LangChain + Groq")

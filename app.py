# app.py

import streamlit as st
from sympy import python
from agents import AgentManager
from utils.logger import logger
import os
from dotenv import load_dotenv
import fitz
# Load environment variables from .env if present
load_dotenv()

def apply_theme(theme):
    if theme == "Dark":
        bg = "#0F172A"
        text = "#F8FAFC"
        card = "#1E293B"
        border = "#334155"

    else:
        bg = "#F8FAFC"
        text = "#0F172A"
        card = "#FFFFFF"
        border = "#CBD5E1"

    st.markdown(
        f"""
        <style>

        /* =========================
           GLOBAL APP BACKGROUND
        ========================= */

        .stApp {{
            background-color: {bg} !important;
            color: {text} !important;
        }}

        html, body {{
            background-color: {bg} !important;
            color: {text} !important;
        }}

        /* FORCE ALL TEXT VISIBILITY */
        * {{
            color: {text} !important;
        }}

        /* =========================
           HERO SECTION
        ========================= */

        .hero {{
            background: linear-gradient(135deg,#4F46E5,#7C3AED);
            padding: 2.5rem;
            border-radius: 24px;
            text-align: center;
            color: white !important;
            margin-bottom: 20px;
        }}

        .hero * {{
            color: white !important;
        }}

        /* =========================
           CARDS
        ========================= */

        .glass {{
            background: {card} !important;
            border: 1px solid {border} !important;
            border-radius: 20px;
            padding: 20px;
            box-shadow: 0 8px 30px rgba(0,0,0,0.15);
            color: {text} !important;
        }}

        .metric-card {{
            background: {card} !important;
            border: 1px solid {border} !important;
            border-radius: 16px;
            padding: 15px;
            text-align: center;
            color: {text} !important;
        }}

        /* =========================
           SIDEBAR FIX
        ========================= */

        section[data-testid="stSidebar"] {{
            background-color: {card} !important;
        }}

        section[data-testid="stSidebar"] * {{
            color: {text} !important;
        }}

        /* =========================
           INPUT FIELDS FIX
        ========================= */

        input, textarea {{
            background-color: {card} !important;
            color: {text} !important;
            border: 1px solid {border} !important;
        }}

        /* =========================
           BUTTON FIX
        ========================= */

        .stButton > button {{
            width: 100%;
            height: 50px;
            border-radius: 12px;
            font-weight: 700;
            background-color: {card} !important;
            color: {text} !important;
            border: 1px solid {border} !important;
        }}

        /* =========================
           TABS FIX (IMPORTANT FOR YOU)
        ========================= */

        button[data-baseweb="tab"] {{
            color: {text} !important;
        }}

        /* selected tab indicator */
        div[data-baseweb="tab-highlight"] {{
            background-color: #4F46E5 !important;
        }}

        /* =========================
           STREAMLIT COMPONENT FIX
        ========================= */

        div[data-testid="stMetric"] {{
            background-color: {card} !important;
            color: {text} !important;
        }}

        div[data-testid="stExpander"] {{
            background-color: {card} !important;
            color: {text} !important;
        }}

        </style>
        """,
        unsafe_allow_html=True,
    )
def pdf_research_section(agent_manager):

    st.header("📄 PDF Research Assistant")

    uploaded_file = st.file_uploader(
        "Upload Research Paper",
        type=["pdf"]
    )

    if uploaded_file:

        text = extract_pdf_text(uploaded_file)

        st.success("PDF uploaded successfully")

        with st.expander("Preview Extracted Text"):
            st.write(text[:3000])

        if st.button("Generate Summary"):

            summarizer = agent_manager.get_agent(
                "summarize"
            )

            summary = summarizer.execute(text)

            st.subheader("Summary")

            st.write(summary)

        question = st.text_input(
            "Ask a question about this PDF"
        )

        if st.button("Ask PDF"):

            prompt = f"""
            Based on the following document:

            {text[:15000]}

            Answer:

            {question}
            """

            qa_agent = agent_manager.get_agent(
                "write_article"
            )

            answer = qa_agent.call_llm([
                {
                    "role":"user",
                    "content":prompt
                }
            ])

            st.subheader("Answer")

            st.write(answer)


def render_dashboard():
    st.markdown(
        """
        <div class="hero">
            <h1>🤖 Multi-Agent AI Platform</h1>
            <h4>Summarization • Research Generation • PHI Sanitization</h4>
            <p>Powered by Gemini + Multi-Agent Architecture</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("Agents", "6")

    with c2:
        st.metric("Tasks", "3")

    with c3:
        st.metric("Validation", "100%")

    with c4:
        st.metric("Status", "🟢 Online")

    st.markdown("---")

def main():

    st.set_page_config(
        page_title="Multi-Agent AI System",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    theme = st.sidebar.toggle(
        "🌙 Dark Mode",
        value=True
    )

    apply_theme(
        "Dark" if theme else "Light"
    )

    render_dashboard()

    st.sidebar.title("⚙️ Settings")

    agent_manager = AgentManager(
        max_retries=2,
        verbose=True
    )

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "📄 Summarization",
            "✍️ Research Writer",
            "🔒 PHI Sanitizer",
            "📚 PDF Research Assistant"
        ]
    )

    with tab1:
        summarize_section(agent_manager)

    with tab2:
        write_and_refine_article_section(agent_manager)

    with tab3:
        sanitize_data_section(agent_manager)

    with tab4:
        pdf_research_section(agent_manager)

def summarize_section(agent_manager):
    st.header("Summarize Medical Text")
    text = st.text_area("Enter medical text to summarize:", height=200)
    if st.button("Summarize"):
        if text:
            main_agent = agent_manager.get_agent("summarize")
            validator_agent = agent_manager.get_agent("summarize_validator")
            with st.spinner("Summarizing..."):
                try:
                    summary = main_agent.execute(text)
                    st.subheader("Summary:")
                    st.write(summary)
                except Exception as e:
                    st.error(f"Error: {e}")
                    logger.error(f"SummarizeAgent Error: {e}")
                    return

            with st.spinner("Validating summary..."):
                try:
                    validation = validator_agent.execute(original_text=text, summary=summary)
                    st.subheader("Validation:")
                    st.write(validation)
                except Exception as e:
                    st.error(f"Validation Error: {e}")
                    logger.error(f"SummarizeValidatorAgent Error: {e}")
        else:
            st.warning("Please enter some text to summarize.")

def extract_pdf_text(pdf_file):
    text = ""

    pdf_bytes = pdf_file.read()

    doc = fitz.open(
        stream=pdf_bytes,
        filetype="pdf"
    )

    for page in doc:
        text += page.get_text()

    return text
def write_and_refine_article_section(agent_manager):
    st.header("Write and Refine Research Article")
    topic = st.text_input("Enter the topic for the research article:")
    outline = st.text_area("Enter an outline (optional):", height=150)
    if st.button("Write and Refine Article"):
        if topic:
            writer_agent = agent_manager.get_agent("write_article")
            refiner_agent = agent_manager.get_agent("refiner")
            validator_agent = agent_manager.get_agent("validator")
            with st.spinner("Writing article..."):
                try:
                    draft = writer_agent.execute(topic, outline)
                    st.subheader("Draft Article:")
                    st.write(draft)
                except Exception as e:
                    st.error(f"Error: {e}")
                    logger.error(f"WriteArticleAgent Error: {e}")
                    return

            with st.spinner("Refining article..."):
                try:
                    refined_article = refiner_agent.execute(draft)
                    st.subheader("Refined Article:")
                    st.write(refined_article)
                except Exception as e:
                    st.error(f"Refinement Error: {e}")
                    logger.error(f"RefinerAgent Error: {e}")
                    return

            with st.spinner("Validating article..."):
                try:
                    validation = validator_agent.execute(topic=topic, article=refined_article)
                    st.subheader("Validation:")
                    st.write(validation)
                except Exception as e:
                    st.error(f"Validation Error: {e}")
                    logger.error(f"ValidatorAgent Error: {e}")
        else:
            st.warning("Please enter a topic for the research article.")


def sanitize_data_section(agent_manager):
    st.header("Sanitize Medical Data (PHI)")
    medical_data = st.text_area("Enter medical data to sanitize:", height=200)
    if st.button("Sanitize Data"):
        if medical_data:
            main_agent = agent_manager.get_agent("sanitize_data")
            validator_agent = agent_manager.get_agent("sanitize_data_validator")
            with st.spinner("Sanitizing data..."):
                try:
                    sanitized_data = main_agent.execute(medical_data)
                    st.subheader("Sanitized Data:")
                    st.write(sanitized_data)
                except Exception as e:
                    st.error(f"Error: {e}")
                    logger.error(f"SanitizeDataAgent Error: {e}")
                    return

            with st.spinner("Validating sanitized data..."):
                try:
                    validation = validator_agent.execute(original_data=medical_data, sanitized_data=sanitized_data)
                    st.subheader("Validation:")
                    st.write(validation)
                except Exception as e:
                    st.error(f"Validation Error: {e}")
                    logger.error(f"SanitizeDataValidatorAgent Error: {e}")
        else:
            st.warning("Please enter medical data to sanitize.")

if __name__ == "__main__":
    main()

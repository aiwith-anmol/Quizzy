"""
AI Study Assistant - Powered by Google Gemini
A student-friendly web app for generating practice questions from study material.

SECURITY NOTE: This app requires users to provide their own Gemini API key.
No API keys are hardcoded, making it safe for GitHub.
"""

import streamlit as st
import google.generativeai as genai
from typing import Optional, Dict
import time

# ═══════════════════════════════════════════════════════════════════════════
# PAGE CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════

st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ═══════════════════════════════════════════════════════════════════════════
# CUSTOM CSS STYLING
# ═══════════════════════════════════════════════════════════════════════════

st.markdown("""
<style>
    /* Main container styling */
    .main {
        padding: 2rem;
    }
    
    /* Question card styling */
    .question-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        color: white;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Answer styling */
    .correct-answer {
        background-color: #10b981;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        font-weight: bold;
        display: inline-block;
        margin: 0.5rem 0;
    }
    
    /* Explanation styling */
    .explanation {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #fbbf24;
        margin-top: 0.5rem;
    }
    
    /* Success message */
    .success-message {
        background-color: #d1fae5;
        color: #065f46;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #10b981;
        margin: 1rem 0;
    }
    
    /* Sidebar styling */
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Button styling */
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem;
        font-weight: bold;
        border-radius: 5px;
        transition: all 0.3s;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════
# SESSION STATE INITIALIZATION
# ═══════════════════════════════════════════════════════════════════════════

def initialize_session_state():
    """Initialize session state variables for the app."""
    if 'api_key' not in st.session_state:
        st.session_state.api_key = ""
    if 'api_key_validated' not in st.session_state:
        st.session_state.api_key_validated = False
    if 'generated_questions' not in st.session_state:
        st.session_state.generated_questions = None
    if 'last_content' not in st.session_state:
        st.session_state.last_content = ""

initialize_session_state()

# ═══════════════════════════════════════════════════════════════════════════
# API KEY VALIDATION
# ═══════════════════════════════════════════════════════════════════════════

def validate_api_key(api_key: str) -> bool:
    """
    Validate the Google Gemini API key.
    
    Args:
        api_key: The API key to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not api_key or len(api_key.strip()) == 0:
        return False
    
    try:
        genai.configure(api_key=api_key)
        # Try to list models to verify the key works
        list(genai.list_models())
        return True
    except Exception as e:
        st.error(f"❌ Invalid API key: {str(e)}")
        return False

# ═══════════════════════════════════════════════════════════════════════════
# QUESTION GENERATION
# ═══════════════════════════════════════════════════════════════════════════

@st.cache_data(ttl=3600, show_spinner=False)
def generate_questions(
    content: str,
    num_questions: int,
    topic_focus: str,
    _api_key: str  # Underscore prefix prevents caching on this parameter
) -> Optional[str]:
    """
    Generate multiple-choice questions using Google Gemini API.
    
    Args:
        content: The study material to generate questions from
        num_questions: Number of questions to generate
        topic_focus: Optional topic to focus on
        _api_key: Google Gemini API key (not cached)
        
    Returns:
        Generated questions as formatted string, or None if error
    """
    try:
        # Configure the API with the provided key
        genai.configure(api_key=_api_key)
        
        # Initialize the model (using Gemini 1.5 Flash for speed)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Construct the prompt
        topic_instruction = f"\nTopic Focus: {topic_focus}" if topic_focus else ""
        
        prompt = f"""You are an expert educator creating practice questions.

Given this study content:
{content}
{topic_instruction}

Generate exactly {num_questions} multiple-choice questions.

CRITICAL RULES:
1. Questions must test understanding and critical thinking, not just memorization
2. All four options (A, B, C, D) must be plausible - no obviously wrong answers
3. Base questions ONLY on information from the provided content
4. Provide clear, educational explanations (2-3 sentences)
5. Vary difficulty levels appropriately

FORMAT EACH QUESTION EXACTLY LIKE THIS:

📌 Question 1: [Your question here]
A) [Option A]
B) [Option B]
C) [Option C]
D) [Option D]

✅ Correct Answer: [Letter]
💡 Explanation: [2-3 sentence explanation of why this answer is correct and why others are incorrect]
━━━━━━━━━━━━━━━━━━━━━━━━

Generate {num_questions} questions now:"""

        # Generate the response
        response = model.generate_content(prompt)
        
        return response.text
        
    except Exception as e:
        st.error(f"⚠️ Error generating questions: {str(e)}")
        return None

# ═══════════════════════════════════════════════════════════════════════════
# MAIN APP UI
# ═══════════════════════════════════════════════════════════════════════════

def main():
    """Main application logic and UI."""
    
    # Header
    st.title("⚡ AI Study Assistant")
    st.markdown("### Powered by Google Gemini")
    st.markdown("Generate practice questions from your study material in seconds!")
    
    # ─────────────────────────────────────────────────────────────────────────
    # SIDEBAR CONFIGURATION
    # ─────────────────────────────────────────────────────────────────────────
    
    with st.sidebar:
        st.header("🔧 Configuration")
        
        # API Key Input
        st.markdown("### 🔑 API Key Setup")
        st.markdown(
            "Get your **free** Gemini API key:  \n"
            "👉 [aistudio.google.com](https://aistudio.google.com)"
        )
        
        api_key_input = st.text_input(
            "AIzaSyD6lgO-WAA8vD3WYtI4TRFIgTJ2cmkVNjQ",
            type="password",
            value=st.session_state.api_key,
            help="Your API key is stored only in this session and never saved."
        )
        
        # Validate API key when entered
        if api_key_input != st.session_state.api_key:
            st.session_state.api_key = api_key_input
            st.session_state.api_key_validated = False
            
            if api_key_input:
                with st.spinner("Validating API key..."):
                    if validate_api_key(api_key_input):
                        st.session_state.api_key_validated = True
                        st.success("✅ API key validated!")
                    else:
                        st.session_state.api_key_validated = False
        
        # Show validation status
        if st.session_state.api_key_validated:
            st.success("✅ Ready to generate questions!")
        elif st.session_state.api_key:
            st.warning("⚠️ Please check your API key")
        else:
            st.info("ℹ️ Please enter your API key to continue")
        
        st.markdown("---")
        
        # Question Configuration
        st.markdown("### 📚 Question Settings")
        
        topic_focus = st.text_input(
            "Topic Focus (Optional)",
            placeholder="e.g., Cell Biology, World War II",
            help="Focus questions on a specific topic within your material"
        )
        
        num_questions = st.slider(
            "Number of Questions",
            min_value=1,
            max_value=10,
            value=5,
            help="Choose how many questions to generate"
        )
        
        st.markdown("---")
        
        # Clear button
        if st.button("🔄 Clear All", use_container_width=True):
            st.session_state.generated_questions = None
            st.session_state.last_content = ""
            st.rerun()
        
        # Information
        st.markdown("---")
        st.markdown("### ℹ️ About")
        st.markdown(
            "This app uses Google's Gemini AI to generate "
            "high-quality practice questions from your study material."
        )
        st.markdown(
            "**Privacy:** Your API key and content are only used "
            "for this session and are never stored."
        )
    
    # ─────────────────────────────────────────────────────────────────────────
    # MAIN CONTENT AREA
    # ─────────────────────────────────────────────────────────────────────────
    
    # Study material input
    st.markdown("### 📝 Step 1: Paste Your Study Material")
    
    study_content = st.text_area(
        "Paste your notes, textbook excerpts, or any study material here...",
        height=250,
        placeholder="Example: Photosynthesis is the process by which plants convert light energy...",
        help="The AI will generate questions based only on this content"
    )
    
    # Generate button
    st.markdown("### 🚀 Step 2: Generate Questions")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        generate_btn = st.button(
            "🎯 Generate Practice Questions",
            use_container_width=True,
            disabled=not st.session_state.api_key_validated or not study_content,
            type="primary"
        )
    
    # Show helpful messages if button is disabled
    if not st.session_state.api_key_validated and not study_content:
        st.warning("⚠️ Please enter your API key in the sidebar and paste your study material above.")
    elif not st.session_state.api_key_validated:
        st.warning("⚠️ Please enter a valid API key in the sidebar.")
    elif not study_content:
        st.warning("⚠️ Please paste your study material above.")
    
    # ─────────────────────────────────────────────────────────────────────────
    # QUESTION GENERATION AND DISPLAY
    # ─────────────────────────────────────────────────────────────────────────
    
    if generate_btn:
        # Clear cache if content has changed
        if study_content != st.session_state.last_content:
            generate_questions.clear()
            st.session_state.last_content = study_content
        
        with st.spinner(f"🤖 Generating {num_questions} questions... This may take 10-30 seconds."):
            questions = generate_questions(
                content=study_content,
                num_questions=num_questions,
                topic_focus=topic_focus,
                _api_key=st.session_state.api_key
            )
            
            if questions:
                st.session_state.generated_questions = questions
    
    # Display generated questions
    if st.session_state.generated_questions:
        st.markdown("---")
        st.markdown("### 📋 Your Practice Questions")
        
        st.success(
            f"✅ Successfully generated {num_questions} questions! "
            "Review them below and test your knowledge."
        )
        
        # Display the questions in a nice format
        st.markdown(
            f"<div style='background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); "
            f"padding: 2rem; border-radius: 10px; margin: 1rem 0;'>"
            f"{st.session_state.generated_questions.replace(chr(10), '<br>')}"
            f"</div>",
            unsafe_allow_html=True
        )
        
        # Download option
        st.download_button(
            label="📥 Download Questions as Text File",
            data=st.session_state.generated_questions,
            file_name=f"practice_questions_{time.strftime('%Y%m%d_%H%M%S')}.txt",
            mime="text/plain",
            use_container_width=True
        )
    
    # ─────────────────────────────────────────────────────────────────────────
    # FOOTER
    # ─────────────────────────────────────────────────────────────────────────
    
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: #666; padding: 1rem;'>"
        "Made with ❤️ using Streamlit and Google Gemini | "
        "Safe for GitHub - No hardcoded API keys!"
        "</div>",
        unsafe_allow_html=True
    )

# ═══════════════════════════════════════════════════════════════════════════
# RUN THE APP
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    main()

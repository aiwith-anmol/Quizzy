"""
AI Study Assistant - Generate Practice Questions from Study Material
Built with Streamlit and Google Gemini API
"""

import streamlit as st
import google.generativeai as genai
import re
from typing import List, Dict

# Page configuration
st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .question-box {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 15px 0;
        border-left: 5px solid #1E88E5;
    }
    .correct-answer {
        background-color: #d4edda;
        padding: 10px;
        border-radius: 5px;
        margin-top: 10px;
    }
    .explanation {
        background-color: #fff3cd;
        padding: 10px;
        border-radius: 5px;
        margin-top: 10px;
    }
    .stButton>button {
        width: 100%;
        background-color: #1E88E5;
        color: white;
        font-size: 1.2rem;
        padding: 0.5rem;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

def initialize_session_state():
    """Initialize session state variables"""
    if 'questions_generated' not in st.session_state:
        st.session_state.questions_generated = False
    if 'generated_questions' not in st.session_state:
        st.session_state.generated_questions = []

def configure_gemini(api_key: str) -> bool:
    """
    Configure Google Gemini API with the provided API key
    
    Args:
        api_key: Google Gemini API key
    
    Returns:
        bool: True if configuration successful, False otherwise
    """
    try:
        genai.configure(api_key=api_key)
        return True
    except Exception as e:
        st.error(f"❌ Error configuring API: {str(e)}")
        return False

def generate_questions(study_material: str, topic: str, num_questions: int, api_key: str) -> List[Dict]:
    """
    Generate practice questions using Google Gemini API
    
    Args:
        study_material: The study notes/content provided by user
        topic: Specific topic to focus on
        num_questions: Number of questions to generate
        api_key: Google Gemini API key
    
    Returns:
        List of question dictionaries
    """
    try:
        # Configure API
        if not configure_gemini(api_key):
            return []
        
        # Initialize the model
        model = genai.GenerativeModel('gemini-pro')
        
        # Create detailed prompt for question generation
        prompt = f"""
You are an expert educator creating practice questions for students.

Based on the following study material about "{topic}", generate exactly {num_questions} multiple-choice questions (MCQs).

Study Material:
{study_material}

Instructions:
1. Create {num_questions} high-quality multiple-choice questions
2. Each question should have 4 options (A, B, C, D)
3. Only ONE option should be correct
4. Provide a brief explanation for the correct answer
5. Questions should test understanding, not just memorization
6. Make questions clear and unambiguous

Format each question EXACTLY as follows:

Question 1: [Your question here]
A) [Option A]
B) [Option B]
C) [Option C]
D) [Option D]
Correct Answer: [A/B/C/D]
Explanation: [Brief explanation of why this is correct]

Question 2: [Your question here]
...and so on.

Generate the questions now:
"""
        
        # Generate content
        with st.spinner('🤖 AI is generating your practice questions...'):
            response = model.generate_content(prompt)
            
            if not response or not response.text:
                st.error("❌ No response from AI. Please try again.")
                return []
            
            # Parse the response
            questions = parse_questions(response.text)
            
            if not questions:
                st.error("❌ Could not parse questions. Please try again.")
                st.expander("Debug: Raw AI Response").write(response.text)
                return []
            
            return questions
            
    except Exception as e:
        st.error(f"❌ Error generating questions: {str(e)}")
        st.info("💡 Tip: Make sure your API key is valid and you have internet connection.")
        return []

def parse_questions(response_text: str) -> List[Dict]:
    """
    Parse the AI response into structured question dictionaries
    
    Args:
        response_text: Raw text response from AI
    
    Returns:
        List of parsed questions
    """
    questions = []
    
    # Split by "Question X:" pattern
    question_blocks = re.split(r'Question \d+:', response_text)
    
    for block in question_blocks[1:]:  # Skip first empty split
        try:
            lines = [line.strip() for line in block.strip().split('\n') if line.strip()]
            
            if len(lines) < 6:  # Need at least: question, 4 options, answer, explanation
                continue
            
            # Extract question text (first line)
            question_text = lines[0]
            
            # Extract options (next 4 lines starting with A), B), C), D))
            options = {}
            option_lines = [l for l in lines if re.match(r'^[A-D]\)', l)]
            
            for opt_line in option_lines[:4]:
                match = re.match(r'^([A-D])\)\s*(.+)', opt_line)
                if match:
                    options[match.group(1)] = match.group(2)
            
            # Extract correct answer
            correct_answer = ""
            for line in lines:
                if line.startswith("Correct Answer:"):
                    correct_answer = re.search(r'[A-D]', line)
                    if correct_answer:
                        correct_answer = correct_answer.group(0)
                    break
            
            # Extract explanation
            explanation = ""
            for line in lines:
                if line.startswith("Explanation:"):
                    explanation = line.replace("Explanation:", "").strip()
                    break
            
            # Only add if we have all components
            if question_text and len(options) == 4 and correct_answer and explanation:
                questions.append({
                    'question': question_text,
                    'options': options,
                    'correct_answer': correct_answer,
                    'explanation': explanation
                })
        
        except Exception as e:
            continue  # Skip malformed questions
    
    return questions

def display_questions(questions: List[Dict]):
    """
    Display generated questions in a formatted way
    
    Args:
        questions: List of question dictionaries
    """
    if not questions:
        st.warning("⚠️ No questions were generated. Please try again with different content.")
        return
    
    st.success(f"✅ Successfully generated {len(questions)} practice questions!")
    st.markdown("---")
    
    for idx, q in enumerate(questions, 1):
        st.markdown(f"""
        <div class="question-box">
            <h3>Question {idx}</h3>
            <p style="font-size: 1.1rem; font-weight: 500;">{q['question']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Display options
        for option_key in ['A', 'B', 'C', 'D']:
            if option_key in q['options']:
                is_correct = option_key == q['correct_answer']
                icon = "✅" if is_correct else "⚪"
                st.markdown(f"{icon} **{option_key})** {q['options'][option_key]}")
        
        # Display correct answer and explanation
        st.markdown(f"""
        <div class="correct-answer">
            <strong>✓ Correct Answer: {q['correct_answer']}</strong>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="explanation">
            <strong>💡 Explanation:</strong> {q['explanation']}
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)

def main():
    """Main application function"""
    
    # Initialize session state
    initialize_session_state()
    
    # Header
    st.markdown('<h1 class="main-header">📚 AI Study Assistant</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Generate practice questions from your study material using AI</p>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.header("⚙️ Settings")
        
        # API Key input
        st.markdown("### 🔑 API Configuration")
        api_key = st.text_input(
            "Enter your Google Gemini API Key",
            type="password",
            help="Get your free API key from https://makersuite.google.com/app/apikey"
        )
        
        if not api_key:
            st.info("👆 Please enter your API key to continue")
            st.markdown("""
            **How to get an API key:**
            1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
            2. Sign in with your Google account
            3. Click "Create API Key"
            4. Copy and paste it above
            
            *The API is free to use!*
            """)
        
        st.markdown("---")
        
        # Topic input
        st.markdown("### 📖 Study Topic")
        topic = st.text_input(
            "What topic are you studying?",
            placeholder="e.g., Photosynthesis, World War II, Calculus",
            help="Specify the main topic for focused question generation"
        )
        
        # Number of questions
        st.markdown("### 🔢 Question Count")
        num_questions = st.slider(
            "How many questions to generate?",
            min_value=3,
            max_value=10,
            value=5,
            help="More questions take longer to generate"
        )
        
        st.markdown("---")
        st.markdown("""
        ### 📝 Tips for Best Results
        - Paste at least 200-300 words
        - Be specific with your topic
        - Use clear, educational content
        - Check the examples below!
        """)
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📄 Your Study Material")
        study_material = st.text_area(
            "Paste your notes, textbook content, or study material here:",
            height=300,
            placeholder="""Example: Photosynthesis is the process by which plants use sunlight, water, and carbon dioxide to create oxygen and energy in the form of sugar. This process occurs in the chloroplasts of plant cells, specifically in the thylakoid membranes and stroma. The light-dependent reactions occur in the thylakoid membranes and produce ATP and NADPH, while the light-independent reactions (Calvin cycle) occur in the stroma and use ATP and NADPH to fix carbon dioxide into glucose...""",
            help="Paste educational content related to your topic"
        )
    
    with col2:
        st.markdown("### 📚 Example Topics")
        st.info("""
        **Science:**
        - Photosynthesis
        - Newton's Laws
        - Cell Division
        
        **History:**
        - World War II
        - Renaissance Period
        - American Revolution
        
        **Math:**
        - Quadratic Equations
        - Calculus Basics
        - Probability Theory
        
        **Literature:**
        - Shakespeare's Works
        - Poetry Analysis
        - Literary Devices
        """)
    
    # Generate button
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("🚀 Generate Practice Questions", type="primary"):
        # Validation
        if not api_key:
            st.error("❌ Please enter your Google Gemini API key in the sidebar.")
        elif not topic:
            st.error("❌ Please specify a study topic in the sidebar.")
        elif not study_material or len(study_material.strip()) < 50:
            st.error("❌ Please provide at least 50 characters of study material.")
        else:
            # Generate questions
            questions = generate_questions(study_material, topic, num_questions, api_key)
            
            if questions:
                st.session_state.generated_questions = questions
                st.session_state.questions_generated = True
    
    # Display results
    if st.session_state.questions_generated and st.session_state.generated_questions:
        st.markdown("---")
        st.markdown("## 🎯 Your Practice Questions")
        display_questions(st.session_state.generated_questions)
        
        # Download option
        if st.session_state.generated_questions:
            # Create downloadable text
            download_text = f"Practice Questions - {topic}\n{'='*50}\n\n"
            for idx, q in enumerate(st.session_state.generated_questions, 1):
                download_text += f"Question {idx}: {q['question']}\n"
                for opt_key in ['A', 'B', 'C', 'D']:
                    if opt_key in q['options']:
                        download_text += f"{opt_key}) {q['options'][opt_key]}\n"
                download_text += f"\nCorrect Answer: {q['correct_answer']}\n"
                download_text += f"Explanation: {q['explanation']}\n\n"
                download_text += "-" * 50 + "\n\n"
            
            st.download_button(
                label="📥 Download Questions as Text File",
                data=download_text,
                file_name=f"{topic.replace(' ', '_')}_questions.txt",
                mime="text/plain"
            )
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; padding: 20px;">
        <p>Made with ❤️ using Streamlit and Google Gemini AI</p>
        <p style="font-size: 0.9rem;">💡 Tip: Generate new questions by modifying your study material or topic!</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

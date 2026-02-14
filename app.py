import streamlit as st

# Check if google.generativeai is available, if not show installation message
try:
    import google.generativeai as genai
    GENAI_AVAILABLE = True
except ImportError:
    GENAI_AVAILABLE = False

import re
from typing import List, Dict

# Page config
st.set_page_config(page_title="Quizzy - AI Study Assistant", page_icon="🧠", layout="wide")

# CSS
st.markdown("""
<style>
    .main-header {font-size: 2.5rem; color: #1E88E5; text-align: center; margin-bottom: 0.5rem;}
    .question-box {background: #f0f2f6; padding: 15px; border-radius: 8px; margin: 10px 0; border-left: 4px solid #1E88E5;}
    .correct {background: #d4edda; padding: 8px; border-radius: 5px; margin-top: 8px;}
    .explanation {background: #fff3cd; padding: 8px; border-radius: 5px; margin-top: 8px;}
</style>
""", unsafe_allow_html=True)

def init_session():
    if 'questions' not in st.session_state:
        st.session_state.questions = []

def generate_questions(material: str, topic: str, count: int, api_key: str) -> List[Dict]:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-pro')
        
        prompt = f"""Generate {count} multiple-choice questions about {topic} from this material:

{material}

Format each question EXACTLY like this:

Question 1: [question text]
A) [option]
B) [option]
C) [option]
D) [option]
Correct Answer: [A/B/C/D]
Explanation: [why this is correct]

Generate all {count} questions now."""

        with st.spinner('Generating questions...'):
            response = model.generate_content(prompt)
            return parse_response(response.text)
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return []

def parse_response(text: str) -> List[Dict]:
    questions = []
    blocks = re.split(r'Question \d+:', text)[1:]
    
    for block in blocks:
        try:
            lines = [l.strip() for l in block.strip().split('\n') if l.strip()]
            if len(lines) < 6:
                continue
            
            q_text = lines[0]
            opts = {}
            
            for line in lines:
                match = re.match(r'^([A-D])\)\s*(.+)', line)
                if match:
                    opts[match.group(1)] = match.group(2)
            
            correct = ""
            explanation = ""
            
            for line in lines:
                if 'Correct Answer:' in line:
                    ans = re.search(r'[A-D]', line)
                    if ans:
                        correct = ans.group(0)
                if 'Explanation:' in line:
                    explanation = line.split('Explanation:', 1)[1].strip()
            
            if q_text and len(opts) == 4 and correct and explanation:
                questions.append({
                    'question': q_text,
                    'options': opts,
                    'correct': correct,
                    'explanation': explanation
                })
        except:
            continue
    
    return questions

def display_questions(questions: List[Dict]):
    if not questions:
        st.warning("No questions generated. Try different content.")
        return
    
    st.success(f"✅ Generated {len(questions)} questions!")
    st.markdown("---")
    
    for i, q in enumerate(questions, 1):
        st.markdown(f'<div class="question-box"><h3>Question {i}</h3><p>{q["question"]}</p></div>', unsafe_allow_html=True)
        
        for opt in ['A', 'B', 'C', 'D']:
            icon = "✅" if opt == q['correct'] else "⚪"
            st.markdown(f"{icon} **{opt})** {q['options'][opt]}")
        
        st.markdown(f'<div class="correct"><strong>Correct: {q["correct"]}</strong></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="explanation"><strong>💡</strong> {q["explanation"]}</div>', unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

# Main app
init_session()

st.markdown('<h1 class="main-header">🧠 Quizzy</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #666;">AI-powered study assistant - Turn notes into practice questions</p>', unsafe_allow_html=True)

# Check if package is available
if not GENAI_AVAILABLE:
    st.error("⚠️ Google Generative AI package not installed!")
    st.info("Add 'google-generativeai' to requirements.txt and redeploy")
    st.stop()

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    
    api_key = st.text_input("Google Gemini API Key", type="password", help="Get free key from https://makersuite.google.com/app/apikey")
    
    if not api_key:
        st.info("👆 Enter API key to start")
        st.markdown("[Get free API key →](https://makersuite.google.com/app/apikey)")
    
    st.markdown("---")
    topic = st.text_input("Study Topic", placeholder="e.g., Photosynthesis")
    count = st.slider("Questions", 3, 10, 5)
    
    st.markdown("---")
    st.caption("💡 Paste 100-500 words for best results")

# Main area
material = st.text_area(
    "📝 Paste your study material:",
    height=250,
    placeholder="Paste your notes, textbook content, or any study material here...",
    help="Minimum 50 characters"
)

if st.button("🚀 Generate Questions", type="primary", use_container_width=True):
    if not api_key:
        st.error("❌ Enter API key in sidebar")
    elif not topic:
        st.error("❌ Enter study topic in sidebar")
    elif len(material) < 50:
        st.error("❌ Add at least 50 characters of study material")
    else:
        questions = generate_questions(material, topic, count, api_key)
        st.session_state.questions = questions

# Display
if st.session_state.questions:
    st.markdown("---")
    display_questions(st.session_state.questions)
    
    # Download
    download_text = f"Quizzy - {topic}\n{'='*50}\n\n"
    for i, q in enumerate(st.session_state.questions, 1):
        download_text += f"Q{i}: {q['question']}\n"
        for o in ['A','B','C','D']:
            download_text += f"{o}) {q['options'][o]}\n"
        download_text += f"Answer: {q['correct']}\n{q['explanation']}\n\n"
    
    st.download_button("📥 Download Questions", download_text, f"{topic}_quiz.txt", "text/plain")

st.markdown("---")
st.markdown("<p style='text-align: center; color: #666;'>Made with ❤️ using Streamlit & Google Gemini</p>", unsafe_allow_html=True)

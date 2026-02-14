# 📖 Complete Setup Guide

This guide will walk you through setting up and using the AI Study Assistant, from installation to your first generated question set.

## 🎯 Prerequisites

Before you begin, ensure you have:
- Python 3.8 or higher installed ([Download here](https://www.python.org/downloads/))
- Basic familiarity with command line/terminal
- A Google account (for free Gemini API key)
- Internet connection

## 📥 Step 1: Download the Project

### Option A: Clone from GitHub
```bash
git clone https://github.com/yourusername/ai-study-assistant.git
cd ai-study-assistant
```

### Option B: Download as ZIP
1. Click the green "Code" button on GitHub
2. Select "Download ZIP"
3. Extract the ZIP file
4. Open terminal/command prompt in the extracted folder

## 🔧 Step 2: Install Dependencies

### Windows
```bash
# Open Command Prompt or PowerShell
pip install -r requirements.txt
```

### macOS/Linux
```bash
# Open Terminal
pip3 install -r requirements.txt
```

### Using Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## 🔑 Step 3: Get Your Gemini API Key

1. **Go to Google AI Studio**
   - Visit: https://aistudio.google.com
   - Sign in with your Google account

2. **Create API Key**
   - Click "Get API Key" in the top right
   - Click "Create API Key in new project" (or select existing project)
   - Copy your API key immediately

3. **Keep Your Key Safe**
   - ⚠️ Don't share it publicly
   - ⚠️ Don't commit it to Git
   - ✅ You'll enter it in the app sidebar

## 🚀 Step 4: Run the Application

```bash
streamlit run study_assistant.py
```

The app should automatically open in your browser at `http://localhost:8501`

If it doesn't open automatically, copy the URL from the terminal and paste it into your browser.

## 🎨 Step 5: Use the App

### First-Time Setup
1. **Enter API Key**
   - In the left sidebar, find "🔑 API Key Setup"
   - Paste your Gemini API key
   - Wait for validation (green checkmark appears)

2. **Configure Settings**
   - (Optional) Enter a topic focus (e.g., "Cell Biology")
   - Choose number of questions (1-10) using the slider

### Generate Questions
1. **Paste Study Material**
   - Copy your notes, textbook excerpts, or study material
   - Paste into the large text area
   - Minimum ~50 words recommended for best results

2. **Generate**
   - Click "🎯 Generate Practice Questions"
   - Wait 10-30 seconds for AI to generate questions
   - Review your questions!

3. **Download**
   - Click "📥 Download Questions as Text File"
   - Save for offline study

### Tips for Best Results
- **Quality Material**: Provide clear, well-structured content
- **Length**: 100-500 words works best
- **Topic Focus**: Use this to narrow down broad content
- **Regenerate**: Clear cache and try again if unsatisfied

## 🔄 Step 6: Stopping the App

Press `Ctrl+C` in the terminal where the app is running.

To run again: `streamlit run study_assistant.py`

## 💡 Optional: Local Development Setup

For developers who want to avoid entering the API key every time:

1. **Create .env file** (already in .gitignore)
   ```bash
   cp .env.example .env
   ```

2. **Edit .env**
   ```env
   GEMINI_API_KEY=your_actual_api_key_here
   ```

3. **Modify code** (study_assistant.py)
   ```python
   # Add at the top
   from dotenv import load_dotenv
   import os
   
   load_dotenv()
   
   # In initialize_session_state():
   if 'api_key' not in st.session_state:
       st.session_state.api_key = os.getenv('GEMINI_API_KEY', '')
   ```

4. **NEVER commit .env to Git!** (already protected by .gitignore)

## 📊 Understanding API Costs

### Free Tier (Google AI Studio)
- 60 requests per minute
- 1,500 requests per day
- Perfect for personal study use

### When You Might Need Paid
- Heavy classroom use (20+ students)
- Generating 50+ question sets per day
- Extremely long study materials

**Current Usage**: Typical student generates 5-10 question sets per study session.

## 🐛 Common Issues and Solutions

### Issue: "ModuleNotFoundError"
**Solution**: Reinstall requirements
```bash
pip install -r requirements.txt --force-reinstall
```

### Issue: "Port 8501 is already in use"
**Solution**: Kill existing Streamlit process or use different port
```bash
streamlit run study_assistant.py --server.port 8502
```

### Issue: "Invalid API key" despite correct key
**Solution**:
1. Generate a new key at https://aistudio.google.com
2. Check for extra spaces when pasting
3. Ensure key starts with "AI" prefix

### Issue: Questions are low quality
**Solution**:
1. Provide more detailed study material
2. Use topic focus to guide the AI
3. Try regenerating (different AI responses)
4. Break very long content into sections

### Issue: Slow generation
**Solution**:
1. Reduce number of questions
2. Shorten study material
3. Check internet speed
4. Normal: 10-30 seconds is typical

## 🔒 Security Checklist

Before sharing your code on GitHub:
- [ ] No API keys in any .py files
- [ ] `.env` is in `.gitignore`
- [ ] `.env` file is NOT committed
- [ ] `secrets.toml` is NOT committed
- [ ] README mentions user-provided keys
- [ ] Users know how to get their own keys

## 📚 Additional Resources

- **Streamlit Docs**: https://docs.streamlit.io
- **Gemini API Docs**: https://ai.google.dev/docs
- **Python-dotenv**: https://pypi.org/project/python-dotenv/
- **Prompt Engineering**: https://ai.google.dev/docs/prompt_best_practices

## 🎓 Educational Use Guidelines

**✅ Appropriate Uses**
- Generating practice questions for self-study
- Creating review materials for exam prep
- Testing understanding of concepts
- Creating study guides

**❌ Inappropriate Uses**
- Generating answers for homework/assignments
- Creating questions from copyrighted textbooks (fair use applies)
- Sharing questions as your original work
- Circumventing academic integrity policies

## 🤝 Getting Help

1. **Check README.md**: Common issues covered
2. **Review this guide**: Step-by-step troubleshooting
3. **GitHub Issues**: Open an issue with:
   - Error message (remove API key if present)
   - Steps to reproduce
   - Your OS and Python version
4. **Community**: Stack Overflow, Reddit r/streamlit

## 🎉 You're Ready!

You should now have:
- ✅ App installed and running
- ✅ API key configured
- ✅ First questions generated
- ✅ Understanding of the workflow

**Happy studying!** 📚✨

---

*Last Updated: February 2026*
*For the latest version, visit: [GitHub Repository URL]*

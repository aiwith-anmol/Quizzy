# ⚡ AI Study Assistant - Powered by Google Gemini

A fast, student-friendly web application that generates high-quality multiple-choice practice questions from your study material using Google's Gemini AI.

## 🎯 Features

- **AI-Powered Question Generation**: Uses Google Gemini 1.5 Flash for fast, intelligent question creation
- **Customizable**: Choose number of questions (1-10) and optional topic focus
- **Safe for GitHub**: No hardcoded API keys - users provide their own
- **Beautiful UI**: Modern, gradient-based design with responsive layout
- **Smart Caching**: Questions are cached for 1 hour to save API calls
- **Download Option**: Save generated questions as text files
- **Error Handling**: Clear error messages and validation

## 🔒 Security Features

This application is **100% safe to publish on GitHub** because:

- ✅ No API keys are hardcoded in the source code
- ✅ Users must provide their own Gemini API key
- ✅ API keys are stored only in session state (never saved to disk)
- ✅ Comprehensive `.gitignore` prevents accidental key commits
- ✅ Clear user instructions for obtaining free API keys

## 🚀 Quick Start

### For Users

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Get Your Free Gemini API Key**
   - Go to [Google AI Studio](https://aistudio.google.com)
   - Sign in with your Google account
   - Click "Get API Key" → "Create API Key"
   - Copy your new API key

3. **Run the Application**
   ```bash
   streamlit run study_assistant.py
   ```

4. **Use the App**
   - Enter your API key in the sidebar
   - Paste your study material in the text area
   - Configure question settings
   - Click "Generate Practice Questions"
   - Review, study, and download your questions!

### For Developers

**Clone and Customize:**
```bash
git clone <your-repo-url>
cd ai-study-assistant
pip install -r requirements.txt
streamlit run study_assistant.py
```

**Optional: Use .env for Local Development**

Create a `.env` file (already in `.gitignore`):
```env
GEMINI_API_KEY=your_api_key_here
```

Modify the code to load from `.env`:
```python
from dotenv import load_dotenv
import os

load_dotenv()
default_key = os.getenv('GEMINI_API_KEY', '')
```

**⚠️ Never commit `.env` files to Git!**

## 📋 Requirements

- Python 3.8 or higher
- Streamlit 1.28.0+
- google-generativeai 0.8.0+
- Internet connection for API calls

## 🎨 Customization Ideas

### 1. Change Color Scheme
Edit the CSS in `study_assistant.py`:
```python
# Current gradient: purple/blue
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

# Try green/teal:
background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);

# Try sunset:
background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
```

### 2. Add More Question Types
Modify the prompt to generate:
- True/False questions
- Fill-in-the-blank
- Short answer questions
- Matching exercises

### 3. Add Difficulty Levels
Add a difficulty selector in the sidebar:
```python
difficulty = st.selectbox(
    "Difficulty Level",
    ["Easy", "Medium", "Hard", "Mixed"]
)
```

### 4. Support File Uploads
Add PDF/DOCX support:
```python
uploaded_file = st.file_uploader("Upload study material", type=['txt', 'pdf', 'docx'])
```

### 5. Add Study Timer
Track how long users spend on each question set.

### 6. Export to Different Formats
Add export options for:
- JSON
- CSV
- Markdown
- Flashcard format (Anki compatible)

## 🔧 How It Works

1. **User Input**: User provides API key and study material
2. **API Configuration**: App configures Gemini API with user's key
3. **Prompt Engineering**: Constructs detailed prompt with specific formatting rules
4. **AI Generation**: Gemini 1.5 Flash model generates questions
5. **Caching**: Results cached for 1 hour to reduce API calls
6. **Display**: Questions formatted and displayed with styling
7. **Download**: Option to save questions for offline study

## 📊 API Usage

- **Model**: Gemini 1.5 Flash (optimized for speed)
- **Typical Cost**: Free tier includes generous quota
- **Rate Limits**: Handled with error messages
- **Caching**: 1-hour TTL reduces redundant API calls

## 🐛 Troubleshooting

**"Invalid API key" Error**
- Verify you copied the entire key from AI Studio
- Check for extra spaces before/after the key
- Generate a new key if needed

**"Rate limit exceeded" Error**
- Wait a few minutes before trying again
- Gemini free tier has rate limits
- Consider upgrading to paid tier for higher limits

**Questions Not Generating**
- Ensure your study material is substantive (50+ words recommended)
- Check your internet connection
- Verify API key is validated (green checkmark)

**Empty or Poor Quality Questions**
- Provide more detailed study material
- Use the topic focus field to guide the AI
- Try regenerating (cache clears after 1 hour)

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Some ideas:
- Add support for more AI models (Claude, GPT)
- Implement quiz mode with scoring
- Add spaced repetition scheduling
- Create mobile-responsive improvements
- Add multi-language support

## ⚠️ Important Notes

- **Privacy**: Your API key and content are never stored permanently
- **Responsibility**: You are responsible for your API usage and costs
- **Content**: Ensure you have rights to the study material you use
- **Academic Integrity**: Use as a study aid, not for cheating

## 📧 Support

For issues or questions:
- Check the troubleshooting section above
- Review [Gemini API documentation](https://ai.google.dev/docs)
- Open an issue on GitHub

---

Made with ❤️ by students, for students. Happy studying! 📚✨

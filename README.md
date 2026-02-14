# 📚 AI Study Assistant

A powerful web application that generates practice questions from study material using Google Gemini AI. Perfect for students who want to test their knowledge and prepare for exams!

## ✨ Features

- **AI-Powered Question Generation**: Uses Google Gemini to create intelligent multiple-choice questions
- **Customizable**: Choose topic focus and number of questions (3-10)
- **Instant Feedback**: Get correct answers and detailed explanations
- **Download Questions**: Save generated questions as a text file
- **User-Friendly Interface**: Clean, intuitive design built with Streamlit
- **Free to Use**: Uses Google's free Gemini API tier

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- A Google Gemini API key (free)

### Installation

1. **Clone or download this repository**

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Get your FREE Google Gemini API Key**
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Sign in with your Google account
   - Click "Create API Key"
   - Copy the API key

4. **Run the application**
```bash
streamlit run app.py
```

5. **Open your browser**
   - The app will automatically open at `http://localhost:8501`
   - If not, navigate to that URL manually

## 📖 How to Use

1. **Enter API Key**: Paste your Google Gemini API key in the sidebar
2. **Specify Topic**: Enter the subject you're studying (e.g., "Photosynthesis")
3. **Choose Question Count**: Select how many questions to generate (3-10)
4. **Paste Study Material**: Add your notes or textbook content (minimum 50 characters)
5. **Generate**: Click the "Generate Practice Questions" button
6. **Review & Download**: Review your questions and download them if needed

## 🌐 Deploy to Streamlit Cloud (FREE)

### Step 1: Prepare Your Repository

1. Create a new repository on GitHub
2. Upload these files:
   - `app.py`
   - `requirements.txt`
   - `README.md` (this file)

### Step 2: Deploy on Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub account
3. Click "New app"
4. Select your repository
5. Set:
   - **Main file path**: `app.py`
   - **Python version**: 3.9 or higher
6. Click "Deploy"

### Step 3: Configure for Public Use

**Important**: For public deployment, you have two options:

#### Option A: Users Enter Their Own API Key (Recommended)
- The app is configured this way by default
- Each user enters their own free Google Gemini API key
- No usage limits or costs for you
- More secure and scalable

#### Option B: Use Streamlit Secrets (Single API Key)
If you want to provide a single API key for all users:

1. In Streamlit Cloud, go to your app settings
2. Click "Secrets"
3. Add:
```toml
GEMINI_API_KEY = "your-api-key-here"
```

4. Modify `app.py` to use secrets:
```python
# Add at the top of main() function:
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
    st.sidebar.success("✅ API key loaded from app secrets")
else:
    api_key = st.text_input(...)  # existing code
```

**Note**: Option B means all users share your API quota. Monitor usage to avoid hitting limits.

## 📋 Example Study Material

```
Photosynthesis is the process by which plants use sunlight, water, and carbon 
dioxide to create oxygen and energy in the form of sugar. This process occurs 
in the chloroplasts of plant cells, specifically in the thylakoid membranes 
and stroma. The light-dependent reactions occur in the thylakoid membranes and 
produce ATP and NADPH, while the light-independent reactions (Calvin cycle) 
occur in the stroma and use ATP and NADPH to fix carbon dioxide into glucose.
```

## 🛠️ Technical Details

### File Structure
```
ai-study-assistant/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

### Dependencies
- **streamlit**: Web application framework
- **google-generativeai**: Google Gemini API client

### How It Works

1. **User Input**: Student provides study material and topic
2. **API Call**: App sends structured prompt to Google Gemini
3. **AI Processing**: Gemini generates questions in specified format
4. **Parsing**: App extracts questions, options, answers, and explanations
5. **Display**: Results shown in formatted, interactive interface
6. **Download**: Option to save questions as text file

## 🔧 Troubleshooting

### "Error configuring API"
- Check that your API key is correct
- Ensure you're connected to the internet
- Verify the API key hasn't expired

### "No response from AI"
- Check your internet connection
- Try reducing the number of questions
- Ensure your study material is sufficient (50+ characters)

### "Could not parse questions"
- Try rephrasing your study material
- Use more structured, educational content
- Check the debug output in the expander

### Questions not generating
- Verify API key is entered correctly
- Ensure topic field is filled
- Check that study material is at least 50 characters
- Look at browser console for errors (F12)

## 💡 Tips for Best Results

1. **Provide Quality Content**: Use clear, educational text from reliable sources
2. **Be Specific**: Narrow topics produce better questions (e.g., "Photosynthesis in C3 plants" vs "Plants")
3. **Sufficient Material**: 200-500 words works best
4. **Review Questions**: AI-generated content should be reviewed for accuracy
5. **Start Small**: Try 3-5 questions first, then increase

## 🔒 Privacy & Security

- API keys are entered locally and never stored
- Study material is only sent to Google's Gemini API
- No data is saved on servers
- Each session is independent

## 📊 API Usage Limits

Google Gemini free tier includes:
- 60 requests per minute
- Sufficient for most educational use

For heavy usage, consider Google's paid plans.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## 📄 License

This project is open source and available for educational purposes.

## 🆘 Support

If you encounter issues:
1. Check the troubleshooting section
2. Review your API key and internet connection
3. Try with different study material
4. Check Streamlit Cloud logs (if deployed)

## 🌟 Acknowledgments

- Built with [Streamlit](https://streamlit.io)
- Powered by [Google Gemini AI](https://deepmind.google/technologies/gemini/)
- Made with ❤️ for students everywhere

---

**Happy Studying! 📚✨**

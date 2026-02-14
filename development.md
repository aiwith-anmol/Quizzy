# 🚀 Quick Deployment Guide

## Deploy to Streamlit Cloud in 5 Minutes

### Step 1: Get Your Files Ready
You have 3 essential files:
- ✅ `app.py` - The main application
- ✅ `requirements.txt` - Dependencies
- ✅ `README.md` - Documentation

### Step 2: Create GitHub Repository

1. Go to [github.com](https://github.com)
2. Click "New repository"
3. Name it: `ai-study-assistant`
4. Make it **Public**
5. Click "Create repository"

### Step 3: Upload Files to GitHub

**Option A: Using GitHub Web Interface**
1. Click "uploading an existing file"
2. Drag and drop: `app.py`, `requirements.txt`, `README.md`
3. Click "Commit changes"

**Option B: Using Git Command Line**
```bash
git init
git add app.py requirements.txt README.md .gitignore
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR-USERNAME/ai-study-assistant.git
git push -u origin main
```

### Step 4: Deploy on Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click "Sign in with GitHub"
3. Authorize Streamlit
4. Click "New app"
5. Fill in:
   - **Repository**: `YOUR-USERNAME/ai-study-assistant`
   - **Branch**: `main`
   - **Main file path**: `app.py`
6. Click "Deploy!"

### Step 5: Wait for Deployment (2-3 minutes)

The app will:
- ✅ Install dependencies
- ✅ Start the server
- ✅ Generate a public URL

### Step 6: Share Your App! 🎉

You'll get a URL like: `https://your-app-name.streamlit.app`

Share this with anyone - they can use it for FREE!

## 🔑 Important Notes

### For Public Use:
- **Users enter their own API keys** (default setup)
- No costs for you
- No usage limits
- Most secure option

### Get Free Google Gemini API Key:
1. Visit: https://makersuite.google.com/app/apikey
2. Sign in with Google
3. Click "Create API Key"
4. Copy and paste in the app

## 📱 Using Your App

1. Open your Streamlit app URL
2. Enter API key in sidebar
3. Paste study material
4. Click "Generate Questions"
5. Review and download!

## 🔧 Updating Your App

Make changes to `app.py` and:

```bash
git add app.py
git commit -m "Update app"
git push
```

Streamlit Cloud will automatically redeploy!

## 💡 Pro Tips

1. **Custom Domain**: Streamlit lets you use custom domains (Pro plan)
2. **Analytics**: Check usage in Streamlit Cloud dashboard
3. **Secrets**: Use Streamlit Secrets for sensitive config
4. **Monitoring**: Set up email alerts for app issues

## ⚡ Common Issues

### "Module not found"
- Check `requirements.txt` has all dependencies
- Redeploy the app

### "App not loading"
- Check Streamlit Cloud logs
- Verify Python version compatibility

### "API errors"
- User needs valid Gemini API key
- Check internet connection

## 🎓 Next Steps

1. ✅ Deploy your app
2. ✅ Test it thoroughly
3. ✅ Share with students
4. ✅ Gather feedback
5. ✅ Iterate and improve!

---

**Need help?** Check the main README.md or Streamlit documentation.

**Happy deploying! 🚀**

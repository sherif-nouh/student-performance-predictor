# 🚀 START HERE - Windows Users

## ⚡ Super Quick Start (3 Steps)

### Step 1: Make Sure You Have Everything
Your folder should look like this:
```
Ai_Project/
├── app.py
├── templates/
│   └── index.html     ← IMPORTANT: Must be inside templates folder!
├── START_HERE.bat     ← This is the easiest way to run
└── (other files...)
```

### Step 2: Run the App
**Double-click: `START_HERE.bat`**

This file will:
1. ✅ Check if all files are in the right place
2. ✅ Start the Flask server
3. ✅ Tell you if something is wrong

### Step 3: Open in Browser
Once you see "Running on http://127.0.0.1:5000", open your browser to:
```
http://localhost:5000
```

🎉 Done! You should see a purple-gradient web interface!

---

## 📝 If You See an Error

### Error: "TemplateNotFound: index.html"
**Problem:** The templates folder or index.html is in the wrong place.

**Solution:**
1. Make sure you have a folder called `templates` (lowercase)
2. Make sure `index.html` is INSIDE the `templates` folder
3. The `templates` folder should be in the same directory as `app.py`

**Check with this structure:**
```
Your Folder/
├── app.py              ← Here
└── templates/          ← Same level as app.py
    └── index.html      ← Inside templates
```

### Error: "Python was not found"
**Problem:** Python is not installed or not in your system PATH.

**Solution:**
1. Download Python from: https://www.python.org/downloads/
2. During installation, CHECK the box "Add Python to PATH"
3. Restart Command Prompt
4. Try again

**Or install from Microsoft Store:**
1. Open Microsoft Store
2. Search for "Python 3.12"
3. Click Install
4. Try again

### Error: "No module named 'flask'"
**Problem:** Flask is not installed.

**Solution:**
```cmd
pip install Flask
```

Then try running `START_HERE.bat` again.

---

## 🔍 Verify Your Setup

Run this before starting the app:
```cmd
python verify_structure.py
```

This will check if everything is set up correctly and tell you what's missing.

---

## 📁 Complete File List

After downloading, you should have:

**Main Files:**
- `app.py` - The Flask application
- `START_HERE.bat` - Easiest way to run (double-click this!)
- `run_app.bat` - Alternative startup script
- `verify_structure.py` - Check if setup is correct

**The Critical Folder:**
- `templates/` folder containing `index.html`

**Documentation:**
- `README_FIRST.md` - This file
- `WINDOWS_SETUP.md` - Detailed Windows guide
- `FILE_STRUCTURE.md` - Folder structure guide
- `README.md` - Full documentation
- `QUICKSTART.md` - Quick reference

**Optional:**
- `test_api.py` - API testing script
- `requirements.txt` - Dependencies list

---

## 🎯 What to Do After Starting

Once the app is running:

1. **Fill in Student Data:**
   - Demographics (age, gender)
   - Family background
   - Academic performance
   - Study habits

2. **Click "Predict Performance"**
   - See the predicted grade (0-20)
   - View performance category
   - Check confidence score

3. **Try Different Scenarios:**
   - Use "Reset Form" to test different students
   - See how different factors affect predictions

---

## 💡 Example Students to Test

### Test 1: High Achiever
- Study time: 20 hours/week
- Past failures: 0
- Absences: 2
- G1: 18, G2: 19
- Result: Should predict ~18-19 (Excellent)

### Test 2: Average Student
- Study time: 10 hours/week
- Past failures: 1
- Absences: 10
- G1: 12, G2: 13
- Result: Should predict ~12-13 (Good)

### Test 3: Struggling Student
- Study time: 5 hours/week
- Past failures: 3
- Absences: 25
- G1: 8, G2: 9
- Result: Should predict ~8-10 (Needs Improvement)

---

## 🛑 Stopping the App

- If running from batch file: Just close the window
- If running from Command Prompt: Press `Ctrl + C`

---

## 📞 Need More Help?

**Check these files in order:**
1. `FILE_STRUCTURE.md` - If you have folder structure issues
2. `WINDOWS_SETUP.md` - For detailed Windows instructions
3. `README.md` - For complete documentation

**Common Issues:**
- Missing templates folder → See `FILE_STRUCTURE.md`
- Python not found → See `WINDOWS_SETUP.md` section "First-Time Setup"
- Can't access in browser → Try `http://127.0.0.1:5000`

---

## ✅ Quick Checklist

Before running:
- [ ] Downloaded all files
- [ ] Templates folder exists
- [ ] index.html is inside templates folder
- [ ] app.py is in the same folder as templates/

To run:
- [ ] Double-click `START_HERE.bat`
- [ ] Wait for "Running on http://127.0.0.1:5000"
- [ ] Open browser to `http://localhost:5000`

---

**Having issues? Run `python verify_structure.py` first to diagnose!**

**Ready? Double-click `START_HERE.bat` to begin!** 🚀

---

*DS510 - Artificial Intelligence Course*  
*Cairo University*

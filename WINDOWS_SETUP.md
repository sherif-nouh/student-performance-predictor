# 🪟 Windows Setup Guide - Student Performance Predictor

## ⚡ Quick Start (Windows)

### Method 1: Double-click to run (Easiest!)
1. Find the file `run_app.bat` in your folder
2. **Double-click** `run_app.bat`
3. A window will open showing "Running on http://127.0.0.1:5000"
4. Open your browser and go to: `http://localhost:5000`

### Method 2: Command Prompt
1. Open Command Prompt (press `Win + R`, type `cmd`, press Enter)
2. Navigate to your folder:
   ```cmd
   cd C:\Users\lsarah\Downloads\Ai_Project
   ```
3. Run the app:
   ```cmd
   python app.py
   ```
4. Open browser to: `http://localhost:5000`

---

## 🔧 First-Time Setup

### Check if Python is installed
Open Command Prompt and type:
```cmd
python --version
```

**If you see something like "Python 3.x.x"** → You're good! Skip to "Running the App"

**If you see "Python was not found"** → Follow these steps:

#### Option A: Install Python from Microsoft Store (Easiest)
1. Press `Win + S` and search for "Microsoft Store"
2. Search for "Python 3.12" or "Python 3.11"
3. Click "Get" or "Install"
4. Wait for installation to complete
5. Restart Command Prompt

#### Option B: Download from python.org
1. Go to https://www.python.org/downloads/
2. Click "Download Python 3.x.x"
3. **IMPORTANT**: Check "Add Python to PATH" during installation
4. Click "Install Now"
5. Restart Command Prompt

---

## 🚀 Running the App

### Easiest Way: Double-click `run_app.bat`
Just double-click the file and it will:
- Start the Flask server
- Show you the URL
- Keep running until you close the window

### Using Command Prompt:
```cmd
cd C:\Users\lsarah\Downloads\Ai_Project
python app.py
```

You should see:
```
* Serving Flask app 'app'
* Debug mode: on
* Running on http://127.0.0.1:5000
```

**This is GOOD!** Your app is running.

---

## 🌐 Opening in Browser

Once the app is running, open your web browser (Chrome, Edge, Firefox) and type:
```
http://localhost:5000
```

You should see a beautiful purple-gradient interface! 🎨

---

## 📝 Using the Web App

### The Form
Fill in student information across 4 sections:

**1. Demographics**
- Age (15-22)
- Gender (Male/Female)
- In Relationship (Yes/No)

**2. Family Background**
- Family Size
- Parent Status (Together/Apart)
- Mother's Education Level (0-4)
- Father's Education Level (0-4)

**3. Academic Factors**
- Study Time (hours per week)
- Past Failures (0-4)
- Absences (0-50)
- First Period Grade (G1: 0-20)
- Second Period Grade (G2: 0-20)
- Travel Time (1-4)

**4. Additional Factors**
- Extra Activities (Yes/No)
- Internet Access (Yes/No)

### Get Predictions
1. Click the **"Predict Performance"** button
2. Wait a moment while the model analyzes
3. See results with:
   - Predicted final grade (0-20)
   - Performance category (color-coded)
   - Model confidence percentage

### Test Different Scenarios
Use the **"Reset Form"** button to try different student profiles

---

## 💡 Example Test Cases

### Test Case 1: Excellent Student
```
Age: 18
Study Time: 20 hours/week
Failures: 0
Absences: 2
G1: 18, G2: 19
Mother Education: 4
Father Education: 4
Internet: Yes
Activities: Yes

Expected Result: Grade 18-19 (Excellent) 🟢
```

### Test Case 2: Average Student
```
Age: 17
Study Time: 10 hours/week
Failures: 1
Absences: 10
G1: 12, G2: 13
Mother Education: 2
Father Education: 2
Internet: Yes
Activities: No

Expected Result: Grade 12-13 (Good) 🟣
```

### Test Case 3: Struggling Student
```
Age: 19
Study Time: 5 hours/week
Failures: 3
Absences: 25
G1: 8, G2: 9
Mother Education: 1
Father Education: 1
Internet: No
Activities: No

Expected Result: Grade 8-10 (Needs Improvement) 🔴
```

---

## ❌ Troubleshooting

### Problem: "Python was not found"
**Solution:** Install Python using one of the methods above, then restart Command Prompt

### Problem: "No module named 'flask'"
**Solution:** Install Flask:
```cmd
pip install Flask
```

### Problem: "Address already in use"
**Solution:** Port 5000 is busy. Close any other programs using it, or:
1. Open `app.py` in Notepad
2. Find the last line: `app.run(debug=True, host='0.0.0.0', port=5000)`
3. Change `5000` to `8080`
4. Save and run again
5. Open browser to `http://localhost:8080`

### Problem: Browser shows "Can't reach this page"
**Solutions to try:**
- Make sure the Command Prompt window is still open and showing Flask running
- Try `http://127.0.0.1:5000` instead
- Check Windows Firewall isn't blocking it
- Try a different browser

### Problem: The page loads but prediction doesn't work
**Solution:** 
- Press `F12` in browser to open Developer Tools
- Click "Console" tab
- Look for any red error messages
- Check the Command Prompt for Python errors

---

## 🛑 Stopping the App

### If using run_app.bat:
- Just close the window

### If using Command Prompt:
- Press `Ctrl + C` in the Command Prompt window
- Type `Y` if asked to confirm

---

## 📁 File Structure

Your folder should look like:
```
Ai_Project/
├── app.py                 ← Main application
├── requirements.txt       ← Dependencies list
├── run_app.bat           ← Windows startup script (double-click this!)
├── README.md             ← Full documentation
├── SETUP.md              ← This file
├── templates/
│   └── index.html        ← Web interface
└── test_api.py           ← Testing script (optional)
```

---

## 🎯 Performance Categories Explained

The app predicts a grade from 0-20 and categorizes it:

| Grade Range | Category | Badge Color |
|-------------|----------|-------------|
| 16-20 | Excellent | 🟢 Green |
| 14-16 | Very Good | 🔵 Blue |
| 12-14 | Good | 🟣 Purple |
| 10-12 | Satisfactory | 🟠 Orange |
| 0-10 | Needs Improvement | 🔴 Red |

---

## 🔄 Integrating Your Real Model (Later)

Right now the app uses a **mock prediction model** for testing. When ready to use your actual Random Forest model:

### Step 1: Save your trained model
```python
import joblib
joblib.dump(model, 'model.pkl')
joblib.dump(scaler, 'scaler.pkl')
```

### Step 2: Place model files in the same folder as app.py
```
Ai_Project/
├── app.py
├── model.pkl          ← Your trained model
├── scaler.pkl         ← Your scaler
└── templates/
```

### Step 3: Update app.py
Open `app.py` in Notepad and add near the top:
```python
import joblib
import pandas as pd

# Load your models
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')
```

Then update the `predict_performance()` function with your preprocessing code.

---

## ✅ Checklist

Before running:
- [ ] Python is installed
- [ ] All files are in the same folder
- [ ] You're in the correct directory in Command Prompt

To run:
- [ ] Double-click `run_app.bat` OR run `python app.py`
- [ ] See "Running on http://127.0.0.1:5000" message
- [ ] Open browser to `http://localhost:5000`

---

## 🎓 Tips for Your DS510 Project

1. **Test thoroughly** with different student profiles
2. **Take screenshots** of the interface and results for your report
3. **Document** the mock model vs. real model performance
4. **Consider adding** feature importance visualization
5. **Use this** as your deployment demonstration

---

**Need help? Common issues and solutions are in the Troubleshooting section above!**

**Ready to start? Double-click `run_app.bat` and open `http://localhost:5000`** 🚀

---

*Created for DS510 - Artificial Intelligence Course*  
*Cairo University - Faculty of Graduate Studies for Statistical Research*

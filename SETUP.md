# 🚀 Student Performance Predictor - Setup Guide

## Quick Start (3 Steps)

### Step 1: Navigate to the folder
```bash
cd /path/to/your/web-app-folder
```

### Step 2: Run the application
```bash
python3 app.py
```

### Step 3: Open in browser
Open your web browser and go to:
```
http://localhost:5000
```

That's it! 🎉

---

## Understanding the Installation

### ✅ Good News
Flask and all dependencies are already installed on your system. The warning message you saw is **normal and can be ignored** - it's just pip's dependency resolver being cautious, but everything installed successfully.

### What the warning means:
- `python-lsp-black` (a code formatting tool) wants a newer version of `black`
- This does NOT affect our web app at all
- Flask, Werkzeug, and all required packages installed successfully

---

## Full Instructions

### Option A: Direct Run (Recommended)
```bash
python3 app.py
```

**You'll see:**
```
* Serving Flask app 'app'
* Debug mode: on
* Running on http://127.0.0.1:5000
```

This is GOOD! Your app is running.

### Option B: Using the startup script
```bash
chmod +x run_app.sh
./run_app.sh
```

---

## Using the Web App

### 1. Open your browser
Go to: `http://localhost:5000`

### 2. Fill in student information
The form has 4 sections:
- **Demographics**: Age, gender, relationship status
- **Family Background**: Family size, parent education levels
- **Academic Factors**: Study time, failures, absences, grades
- **Additional Factors**: Activities, internet access

### 3. Click "Predict Performance"
You'll see:
- Predicted final grade (0-20 scale)
- Performance category with color coding
- Model confidence percentage
- Timestamp

### 4. Try different scenarios
Use the "Reset Form" button to test different student profiles

---

## Example Test Cases

### High Performer
```
Study time: 20 hours/week
Failures: 0
Absences: 2
G1: 18, G2: 19
Expected: Grade ~18-19 (Excellent)
```

### Average Student
```
Study time: 10 hours/week
Failures: 1
Absences: 10
G1: 12, G2: 13
Expected: Grade ~12-13 (Good)
```

### Struggling Student
```
Study time: 5 hours/week
Failures: 3
Absences: 25
G1: 8, G2: 9
Expected: Grade ~8-10 (Needs Improvement)
```

---

## Testing the API (Optional)

### Using curl:
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "age": 18,
    "gender": "Male",
    "studytime": 15,
    "failures": 0,
    "absences": 3,
    "g1": 15,
    "g2": 16,
    "famsize": "GT3 (>3)",
    "pstatus": "Together",
    "medu": 4,
    "fedu": 3,
    "traveltime": 2,
    "activities": "Yes",
    "internet": "Yes",
    "romantic": "No"
  }'
```

### Using Python test script:
```bash
# Terminal 1: Start the server
python3 app.py

# Terminal 2: Run tests
python3 test_api.py
```

---

## Troubleshooting

### ❌ "Address already in use" error
Port 5000 is busy. Either:

**Option 1:** Kill the existing process
```bash
lsof -i :5000
kill -9 <PID>
```

**Option 2:** Use a different port
Edit `app.py`, change the last line:
```python
app.run(debug=True, host='0.0.0.0', port=8080)  # Changed to 8080
```

### ❌ Can't access in browser
Try these URLs:
- `http://localhost:5000`
- `http://127.0.0.1:5000`
- `http://0.0.0.0:5000`

### ❌ Import errors
```bash
pip install Flask --break-system-packages
```

### ✅ The dependency warning is normal!
If you see warnings about `python-lsp-black` or `black` versions, **ignore them**. They don't affect this app.

---

## Integrating Your Real Model

Currently using a **mock model**. To use your Random Forest:

### 1. Save your model files
```python
import joblib
joblib.dump(model, 'model.pkl')
joblib.dump(scaler, 'scaler.pkl')
```

### 2. Update app.py
Add at the top:
```python
import joblib
import pandas as pd

# Load your models
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')
```

### 3. Update predict_performance()
```python
def predict_performance(features):
    # Convert to DataFrame with correct feature names
    df = pd.DataFrame([features])
    
    # Apply your preprocessing
    df_processed = preprocess(df)  # Your preprocessing function
    
    # Scale
    X_scaled = scaler.transform(df_processed)
    
    # Predict
    prediction = model.predict(X_scaled)[0]
    confidence = model.predict_proba(X_scaled).max()
    
    return {
        'predicted_grade': float(prediction),
        'confidence': float(confidence),
        # ... rest of the response
    }
```

---

## Files Included

```
📁 your-web-app/
├── 📄 app.py                 # Main Flask application
├── 📄 requirements.txt       # Dependencies (already satisfied!)
├── 📄 README.md             # Detailed documentation
├── 📄 QUICKSTART.md         # Quick reference
├── 📄 SETUP.md              # This file
├── 📄 run_app.sh            # Startup script
├── 📄 test_api.py           # API testing
└── 📁 templates/
    └── 📄 index.html        # Web interface
```

---

## Performance Categories

| Grade | Category | Color |
|-------|----------|-------|
| 16-20 | Excellent | 🟢 Green |
| 14-16 | Very Good | 🔵 Blue |
| 12-14 | Good | 🟣 Purple |
| 10-12 | Satisfactory | 🟠 Orange |
| 0-10 | Needs Improvement | 🔴 Red |

---

## Tips

✅ **DO:**
- Test with various student profiles
- Use the browser developer tools (F12) to debug
- Check the terminal for Flask logs
- Try the example test cases above

❌ **DON'T:**
- Worry about the pip dependency warnings
- Use this in production without WSGI server (gunicorn/uwsgi)
- Forget to stop the server (Ctrl+C) before closing terminal

---

## Need Help?

1. **Check the terminal** where Flask is running for error messages
2. **Open browser console** (F12 → Console tab) for JavaScript errors
3. **Test the API** using curl or test_api.py
4. **Verify Flask is running** - you should see "Running on http://127.0.0.1:5000"

---

**Ready to test your Student Performance Predictor? Just run:**
```bash
python3 app.py
```

Then open `http://localhost:5000` in your browser! 🎓✨

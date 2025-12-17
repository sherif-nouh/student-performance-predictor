# Quick Start Guide

## Running the Web App

### Option 1: Using the startup script
```bash
./run_app.sh
```

### Option 2: Direct Python command
```bash
python app.py
```

The app will be available at: **http://localhost:5000**

## What You'll See

### Main Interface
- **Header**: Purple gradient with app title
- **Form Sections**:
  1. Demographics (age, gender, relationship)
  2. Family Background (family size, parent education)
  3. Academic Factors (study time, grades, absences)
  4. Additional Factors (activities, internet access)
- **Buttons**: 
  - "Predict Performance" (purple gradient)
  - "Reset Form" (white with purple border)

### Results Display
After clicking "Predict Performance", you'll see:
- **Large number**: Predicted final grade (0-20)
- **Color-coded badge**: Performance category
  - Green: Excellent (16-20)
  - Blue: Very Good (14-16)
  - Purple: Good (12-14)
  - Orange: Satisfactory (10-12)
  - Red: Needs Improvement (0-10)
- **Confidence score**: Model confidence percentage
- **Additional info**: Timestamp, grade scale, model type

## Testing the API

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

### Using the test script:
```bash
# In one terminal
python app.py

# In another terminal
python test_api.py
```

## Example Input Values

### High-performing student:
- Study time: 20 hours/week
- Failures: 0
- Absences: 2
- G1: 18, G2: 19
- Parent education: 4 (higher education)
- Internet access: Yes

**Expected**: Grade 18-19, Category "Excellent"

### Average student:
- Study time: 10 hours/week
- Failures: 1
- Absences: 10
- G1: 12, G2: 13
- Parent education: 2 (middle school)
- Internet access: Yes

**Expected**: Grade 12-13, Category "Good"

### Struggling student:
- Study time: 5 hours/week
- Failures: 3
- Absences: 25
- G1: 8, G2: 9
- Parent education: 1 (primary school)
- Internet access: No

**Expected**: Grade 8-10, Category "Needs Improvement"

## Troubleshooting

### Port 5000 already in use:
```bash
# Find and kill the process
lsof -i :5000
kill -9 <PID>
```

### Module not found:
```bash
pip install -r requirements.txt --break-system-packages
```

### Can't access from browser:
- Check if the server is running (you should see Flask output)
- Try http://127.0.0.1:5000 instead of localhost
- Check firewall settings

## Next Steps

1. **Test with different inputs** to see how the mock model responds
2. **Replace the mock model** with your actual Random Forest model
3. **Add your preprocessing pipeline** to match your training process
4. **Deploy to production** when ready

---

Enjoy testing your Student Performance Predictor! 🎓

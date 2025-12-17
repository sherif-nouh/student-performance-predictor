# Student Performance Predictor - Web Application

A simple, user-friendly web application for testing your student performance prediction model.

## Features

- **Clean, Modern Interface**: Beautiful gradient design with responsive layout
- **Easy Input Form**: Organized sections for demographics, family background, academic factors
- **Real-time Predictions**: Instant prediction results with confidence scores
- **Visual Feedback**: Color-coded performance categories and animated results
- **Mock Model**: Currently uses a mock prediction model - easy to replace with your actual model

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt --break-system-packages
```

### 2. Run the Application

```bash
python app.py
```

The server will start on `http://localhost:5000`

### 3. Access the Application

Open your web browser and navigate to:
```
http://localhost:5000
```

## How to Use

1. **Fill in Student Information**:
   - Demographics (age, gender, relationship status)
   - Family background (size, parent education)
   - Academic factors (study time, grades, absences)
   - Additional factors (activities, internet access)

2. **Click "Predict Performance"**:
   - The system will analyze the data
   - Results appear with animated transition

3. **View Results**:
   - Predicted final grade (0-20 scale)
   - Performance category (Excellent, Very Good, Good, etc.)
   - Model confidence percentage
   - Timestamp of prediction

## Integrating Your Real Model

To use your actual trained model, modify the `predict_performance()` function in `app.py`:

```python
import joblib

# Load your model at startup
model = joblib.load('your_model.pkl')
scaler = joblib.load('your_scaler.pkl')

def predict_performance(features):
    # Convert features to the format your model expects
    feature_array = prepare_features(features)  # Your preprocessing
    
    # Make prediction
    prediction = model.predict(feature_array)
    confidence = model.predict_proba(feature_array).max()
    
    return {
        'predicted_grade': float(prediction[0]),
        'confidence': float(confidence),
        # ... other fields
    }
```

## File Structure

```
.
├── app.py                  # Flask application
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html         # Web interface
└── README.md              # This file
```

## Features to Add

- **Model Upload**: Allow users to upload their own trained models
- **Batch Predictions**: Process multiple students at once
- **Export Results**: Download predictions as CSV/Excel
- **Visualization**: Add charts showing feature importance
- **History**: Save and view past predictions
- **API Documentation**: Add Swagger/OpenAPI docs

## Technical Details

- **Backend**: Flask (Python web framework)
- **Frontend**: Bootstrap 5, Font Awesome icons
- **Prediction Logic**: Currently mock - replace with your Random Forest model
- **Response Format**: JSON API for easy integration

## Performance Categories

| Grade Range | Category | Color |
|-------------|----------|-------|
| 16-20 | Excellent | Green |
| 14-16 | Very Good | Blue |
| 12-14 | Good | Purple |
| 10-12 | Satisfactory | Orange |
| 0-10 | Needs Improvement | Red |

## Notes

- The current implementation uses a mock prediction algorithm
- Default feature values are set for quick testing
- All inputs are validated on both client and server side
- The app is designed for easy model integration

## Next Steps

1. Replace mock prediction with your actual model
2. Test with real student data
3. Deploy to a cloud platform (AWS, Heroku, etc.)
4. Add authentication if needed
5. Implement data logging and analytics

---

**Created for DS510 - Artificial Intelligence Course**
**Cairo University - Faculty of Graduate Studies for Statistical Research**

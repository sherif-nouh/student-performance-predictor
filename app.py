from flask import Flask, render_template, request, jsonify
import numpy as np
from datetime import datetime
import random

app = Flask(__name__)

# Sample feature names based on typical student performance datasets
FEATURES = {
    'age': {'type': 'number', 'label': 'Age', 'min': 15, 'max': 22, 'default': 18},
    'gender': {'type': 'select', 'label': 'Gender', 'options': ['Male', 'Female']},
    'studytime': {'type': 'number', 'label': 'Study Time (hours/week)', 'min': 0, 'max': 40, 'default': 10},
    'failures': {'type': 'number', 'label': 'Past Failures', 'min': 0, 'max': 4, 'default': 0},
    'absences': {'type': 'number', 'label': 'Absences', 'min': 0, 'max': 50, 'default': 5},
    'g1': {'type': 'number', 'label': 'First Period Grade (0-20)', 'min': 0, 'max': 20, 'default': 12},
    'g2': {'type': 'number', 'label': 'Second Period Grade (0-20)', 'min': 0, 'max': 20, 'default': 12},
    'famsize': {'type': 'select', 'label': 'Family Size', 'options': ['LE3 (≤3)', 'GT3 (>3)']},
    'pstatus': {'type': 'select', 'label': 'Parent Status', 'options': ['Together', 'Apart']},
    'medu': {'type': 'number', 'label': 'Mother Education (0-4)', 'min': 0, 'max': 4, 'default': 2},
    'fedu': {'type': 'number', 'label': 'Father Education (0-4)', 'min': 0, 'max': 4, 'default': 2},
    'traveltime': {'type': 'number', 'label': 'Travel Time (1-4)', 'min': 1, 'max': 4, 'default': 2},
    'activities': {'type': 'select', 'label': 'Extra Activities', 'options': ['Yes', 'No']},
    'internet': {'type': 'select', 'label': 'Internet Access', 'options': ['Yes', 'No']},
    'romantic': {'type': 'select', 'label': 'In Relationship', 'options': ['Yes', 'No']},
}

def predict_performance(features):
    """
    Mock prediction function - replace this with your actual model
    This creates a realistic prediction based on input features
    """
    # Extract key features
    studytime = float(features.get('studytime', 10))
    failures = float(features.get('failures', 0))
    absences = float(features.get('absences', 5))
    g1 = float(features.get('g1', 12))
    g2 = float(features.get('g2', 12))
    
    # Simple scoring algorithm for demonstration
    base_score = (g1 + g2) / 2
    
    # Adjust based on other factors
    study_bonus = min(studytime / 4, 3)
    failure_penalty = failures * 2
    absence_penalty = absences / 10
    
    final_score = base_score + study_bonus - failure_penalty - absence_penalty
    final_score = max(0, min(20, final_score))  # Clamp between 0-20
    
    # Add small random variation
    final_score += random.uniform(-0.5, 0.5)
    final_score = round(final_score, 2)
    
    # Determine performance category
    if final_score >= 16:
        category = "Excellent"
        color = "success"
    elif final_score >= 14:
        category = "Very Good"
        color = "info"
    elif final_score >= 12:
        category = "Good"
        color = "primary"
    elif final_score >= 10:
        category = "Satisfactory"
        color = "warning"
    else:
        category = "Needs Improvement"
        color = "danger"
    
    # Calculate confidence (mock)
    confidence = round(random.uniform(0.75, 0.95), 3)
    
    return {
        'predicted_grade': final_score,
        'category': category,
        'color': color,
        'confidence': confidence,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

@app.route('/')
def index():
    return render_template('index.html', features=FEATURES)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        result = predict_performance(data)
        return jsonify({'success': True, 'result': result})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'timestamp': datetime.now().isoformat()})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

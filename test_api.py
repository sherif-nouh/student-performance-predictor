#!/usr/bin/env python3
"""
Test script for the Student Performance Predictor API
"""

import requests
import json

# Test data
test_student = {
    'age': 18,
    'gender': 'Male',
    'studytime': 15,
    'failures': 0,
    'absences': 3,
    'g1': 15,
    'g2': 16,
    'famsize': 'GT3 (>3)',
    'pstatus': 'Together',
    'medu': 4,
    'fedu': 3,
    'traveltime': 2,
    'activities': 'Yes',
    'internet': 'Yes',
    'romantic': 'No'
}

def test_api():
    """Test the prediction API"""
    print("Testing Student Performance Predictor API")
    print("=" * 50)
    
    # Test health endpoint
    print("\n1. Testing health endpoint...")
    try:
        response = requests.get('http://localhost:5000/health')
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response.json()}")
    except Exception as e:
        print(f"   Error: {e}")
        return
    
    # Test prediction endpoint
    print("\n2. Testing prediction endpoint...")
    try:
        response = requests.post(
            'http://localhost:5000/predict',
            json=test_student,
            headers={'Content-Type': 'application/json'}
        )
        print(f"   Status: {response.status_code}")
        result = response.json()
        
        if result.get('success'):
            print("\n   Prediction Results:")
            print(f"   - Predicted Grade: {result['result']['predicted_grade']}")
            print(f"   - Category: {result['result']['category']}")
            print(f"   - Confidence: {result['result']['confidence']*100:.1f}%")
            print(f"   - Timestamp: {result['result']['timestamp']}")
        else:
            print(f"   Error: {result.get('error')}")
    except Exception as e:
        print(f"   Error: {e}")
    
    print("\n" + "=" * 50)
    print("Test completed!")

if __name__ == '__main__':
    print("\nMake sure the Flask server is running on http://localhost:5000")
    print("Run: python app.py (in another terminal)")
    input("\nPress Enter when server is ready...")
    test_api()

#!/usr/bin/env python3
"""
Folder Structure Verification Script
Run this BEFORE running app.py to check if everything is set up correctly
"""

import os
import sys

def check_file_structure():
    """Verify all required files and folders exist"""
    print("=" * 60)
    print("Student Performance Predictor - File Structure Check")
    print("=" * 60)
    print()
    
    all_good = True
    
    # Check current directory
    current_dir = os.getcwd()
    print(f"📁 Current directory: {current_dir}")
    print()
    
    # Required files
    required_files = [
        ('app.py', 'Main application file'),
        ('requirements.txt', 'Dependencies file'),
    ]
    
    # Required folders
    required_folders = [
        ('templates', 'Templates folder (CRITICAL!)'),
    ]
    
    # Files that should be in templates
    template_files = [
        ('templates/index.html', 'Main web page template'),
    ]
    
    print("Checking required files...")
    print("-" * 60)
    for filename, description in required_files:
        if os.path.isfile(filename):
            print(f"✅ Found: {filename} - {description}")
        else:
            print(f"❌ MISSING: {filename} - {description}")
            all_good = False
    
    print()
    print("Checking required folders...")
    print("-" * 60)
    for foldername, description in required_folders:
        if os.path.isdir(foldername):
            print(f"✅ Found: {foldername}/ - {description}")
        else:
            print(f"❌ MISSING: {foldername}/ - {description}")
            all_good = False
    
    print()
    print("Checking template files...")
    print("-" * 60)
    for filepath, description in template_files:
        if os.path.isfile(filepath):
            file_size = os.path.getsize(filepath)
            print(f"✅ Found: {filepath} - {description} ({file_size:,} bytes)")
        else:
            print(f"❌ MISSING: {filepath} - {description}")
            all_good = False
    
    print()
    print("=" * 60)
    
    if all_good:
        print("✅ SUCCESS! All files and folders are in the correct place!")
        print()
        print("You can now run the app:")
        print("  Windows: python app.py")
        print("  Or double-click: run_app.bat")
        print()
        print("Then open your browser to: http://localhost:5000")
    else:
        print("❌ STRUCTURE ERROR! Some files or folders are missing.")
        print()
        print("Please check FILE_STRUCTURE.md for the correct setup.")
        print()
        print("Required structure:")
        print("  Ai_Project/")
        print("  ├── app.py")
        print("  ├── requirements.txt")
        print("  └── templates/")
        print("      └── index.html")
    
    print("=" * 60)
    
    return all_good

if __name__ == '__main__':
    success = check_file_structure()
    if not success:
        sys.exit(1)  # Exit with error code
    sys.exit(0)  # Exit successfully

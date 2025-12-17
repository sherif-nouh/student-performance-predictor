# ⚠️ IMPORTANT: Folder Structure

## ✅ Your folder MUST look like this:

```
Ai_Project/  (or whatever you named your folder)
│
├── app.py                    ← Main Python file
├── requirements.txt          ← Dependencies
├── run_app.bat              ← Windows startup (double-click this!)
├── run_app.sh               ← Linux/Mac startup
├── test_api.py              ← Testing script
│
├── README.md                ← Documentation
├── SETUP.md                 ← Setup guide
├── WINDOWS_SETUP.md         ← Windows guide
├── QUICKSTART.md            ← Quick reference
│
└── templates/               ← THIS FOLDER IS CRITICAL!
    └── index.html           ← Web page template
```

---

## 🔴 Common Mistake: Missing templates folder

### ❌ WRONG - This will NOT work:
```
Ai_Project/
├── app.py
├── index.html              ← WRONG! Can't be here
└── templates/              ← Empty folder
```

### ✅ CORRECT - This WILL work:
```
Ai_Project/
├── app.py
└── templates/              ← Folder exists
    └── index.html          ← File is INSIDE the folder
```

---

## 🔍 How to Check Your Folder Structure

### On Windows:

1. Open File Explorer
2. Navigate to your `Ai_Project` folder
3. You should see:
   - Several `.py`, `.md`, `.bat` files
   - A folder named `templates`
4. **Double-click** the `templates` folder
5. Inside, you should see `index.html`

### Visual Check:
```
📁 Ai_Project/
  📄 app.py
  📄 run_app.bat
  📄 requirements.txt
  📁 templates/
    📄 index.html     ← This file MUST be here!
```

---

## 🚨 If You See "TemplateNotFound" Error

This error means Flask can't find `index.html`. Here's how to fix it:

### Solution 1: Verify Folder Structure
1. Open your `Ai_Project` folder in File Explorer
2. Check if `templates` folder exists at the same level as `app.py`
3. Open the `templates` folder
4. Confirm `index.html` is inside

### Solution 2: Re-download Everything
1. Download ALL files from the outputs
2. Make sure to download the `templates` folder too
3. Keep the folder structure exactly as shown above

### Solution 3: Create templates folder manually
If the `templates` folder is missing:

1. Create a new folder called `templates` (lowercase!)
2. Move `index.html` INTO the `templates` folder
3. The templates folder should be in the same directory as `app.py`

---

## 📋 Verification Checklist

Before running `python app.py`, verify:

- [ ] I can see `app.py` in my folder
- [ ] I can see a folder named `templates` (lowercase)
- [ ] Inside `templates`, there is a file `index.html`
- [ ] I'm running the command from the folder that contains `app.py`

---

## 💻 Running from Command Prompt

### Step 1: Open Command Prompt
- Press `Win + R`
- Type `cmd`
- Press Enter

### Step 2: Navigate to your folder
```cmd
cd C:\Users\lsarah\Downloads\Ai_Project
```
*Replace with your actual path*

### Step 3: Verify you're in the right place
```cmd
dir
```

You should see `app.py` and `templates` folder listed!

### Step 4: Run the app
```cmd
python app.py
```

---

## 🎯 Alternative: Use the Batch File

**Easiest method:**
1. Find `run_app.bat` in your folder
2. **Double-click** it
3. Done!

This automatically runs from the correct directory.

---

## 🆘 Still Having Issues?

### Check your current directory
In Command Prompt, type:
```cmd
cd
```
This shows where you are.

Make sure it shows something like:
```
C:\Users\lsarah\Downloads\Ai_Project
```

### List files in current directory
```cmd
dir
```

You should see:
- `app.py`
- `templates` (with `<DIR>` next to it)
- Other files

### Check if templates folder has index.html
```cmd
dir templates
```

You should see `index.html` listed.

---

## 📦 Complete File List

Your folder should contain these files:

**Python Files:**
- `app.py` (Main application)
- `test_api.py` (Testing script)

**Documentation:**
- `README.md`
- `SETUP.md`
- `WINDOWS_SETUP.md`
- `QUICKSTART.md`
- `FILE_STRUCTURE.md` (this file)

**Configuration:**
- `requirements.txt`
- `run_app.bat` (Windows)
- `run_app.sh` (Linux/Mac)

**Templates Folder:**
- `templates/index.html` ← **MUST be in templates folder!**

---

## 🎓 Quick Test

After downloading everything:

1. Navigate to your folder in Command Prompt
2. Type: `dir templates\index.html`
3. If you see file details → ✅ Structure is correct!
4. If you see "File Not Found" → ❌ Fix the structure

---

**Remember: The `templates` folder is NOT optional. Flask requires it!**

Once your structure is correct, simply run:
```cmd
python app.py
```

Or double-click: `run_app.bat`

Then open: `http://localhost:5000` 🚀

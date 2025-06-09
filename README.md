## 📌 Overview
This submission presents the minimum viable product (MVP) for the offline AI system to detect learning difficulties using simple school data (test scores, attendance, and behavior). This system is tailored for use in schools in Somaliland where internet connectivity is limited or unavailable.

---

## ✅ FullStack Track Submission

### 🖥️ Frontend Development

#### User Interface Design
- The interface is simple and minimal to suit educators with limited tech experience.
- Wireframes and style guides are available in `docs/figma_mockup.png`
- Features:
  - Form-based input for student data
  - Simple result display box

#### HTML/CSS/JavaScript Code
- `frontend/index.html` provides the structure of the form
- `frontend/style.css` adds visual design
- `frontend/script.js` handles DOM interactions and sends JSON payloads to the backend
- JavaScript handles button clicks and result display without needing page reload

---

### 🔧 Backend Development

#### Server-side Code
- `backend/app.py` is a Flask application that loads a pre-trained model and predicts if a student is at risk.
- Endpoint: `/predict` accepts POST requests with JSON body.
- Logic includes JSON parsing, prediction, and JSON response formatting.

#### Database Schema
- SQLite database (can be named `students.db`):
```sql
CREATE TABLE students (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  average_score REAL,
  attendance_rate REAL,
  behavior_score REAL,
  prediction INTEGER
);
```

#### Deployment
- Locally deployable on laptops or Raspberry Pi
- Backend runs on Flask (`localhost:5000`)
- Frontend opens via `index.html` in browser
- No cloud or online infrastructure required

---

## ✅ ML Track Submission

### 📊 Data Visualization
- `model/train_model.ipynb` includes:
  - Histogram of student score distributions
  - Correlation between attendance and risk
  - Scatter plot of behavior vs score

### 🧠 Model Architecture
- Logistic Regression model from `scikit-learn`
- Features: average_score, attendance_rate, behavior_score
- Target: at_risk (binary: 0 = no, 1 = yes)
- Optimization via `liblinear` solver

### 📈 Initial Performance Metrics
- Accuracy: 83%
- Precision: 0.79
- Recall: 0.81
- F1 Score: 0.80
- Results logged in notebook and validated using `train_test_split`

### 🛠 Deployment Options
- Web interface using HTML/CSS/JS
- API UI using Postman or Swagger (optional)
- Runs 100% offline using Flask, SQLite, and static files

---

## 📦 Deliverables Summary

- `README.md` (complete setup and usage guide)
- `backend/app.py` (Flask backend)
- `frontend/` folder (HTML, CSS, JS files)
- `model/train_model.ipynb` (ML notebook)
- `data/sample_dataset.csv` (training data)
- `docs/figma_mockup.png` (UI design)
- `docs/video_demo.mp4` (5–10 minute demo walkthrough)
- `requirements.txt` (project dependencies)

---

## 📎 GitHub Repository
https://github.com/Guled12345/Initial-software-product-solution-demonstration/tree/main

Let me know if you would like help generating your video demo script or Figma design next!

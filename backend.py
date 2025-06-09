from flask import Flask, request, jsonify
import sqlite3
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load the pre-trained ML model
model = pickle.load(open("model.pkl", "rb"))

# Database file path
DB_NAME = "students.db"

# Create the students table if it doesn't exist
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        average_score REAL NOT NULL,
        attendance_rate REAL NOT NULL,
        behavior_score REAL NOT NULL,
        prediction INTEGER NOT NULL
    )
    """)
    conn.commit()
    conn.close()

init_db()

# API endpoint to predict risk and save to DB
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    try:
        name = data["name"]
        average_score = float(data["average_score"])
        attendance_rate = float(data["attendance_rate"])
        behavior_score = float(data["behavior_score"])

        features = np.array([[average_score, attendance_rate, behavior_score]])
        prediction = int(model.predict(features)[0])

        # Save to database
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO students (name, average_score, attendance_rate, behavior_score, prediction)
            VALUES (?, ?, ?, ?, ?)
        """, (name, average_score, attendance_rate, behavior_score, prediction))
        conn.commit()
        conn.close()

        return jsonify({
            "status": "success",
            "student_name": name,
            "risk": prediction
        })
    
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

# Endpoint to get all saved predictions
@app.route("/students", methods=["GET"])
def get_students():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()

    result = []
    for row in rows:
        result.append({
            "id": row[0],
            "name": row[1],
            "average_score": row[2],
            "attendance_rate": row[3],
            "behavior_score": row[4],
            "prediction": row[5]
        })
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)

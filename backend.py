from flask import Flask, request, jsonify
import sqlite3
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    features = np.array([
        data["average_score"],
        data["attendance_rate"],
        data["behavior_score"]
    ]).reshape(1, -1)
    prediction = model.predict(features)
    return jsonify({"risk": int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
    
from flask import Flask, render_template, request, jsonify
import numpy as np
import joblib

app = Flask(__name__)

model = joblib.load("SVR_Model.pkl")
scaler = joblib.load("Scaler_SVR.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    features = np.array([[
        data["Gender"],
        data["Age"],
        data["Height"],
        data["Weight"],
        data["Duration"],
        data["Heart_Rate"],
        data["Body_Temp"]
    ]])

    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)[0]

    return jsonify({"calories": round(float(prediction), 2)})

if __name__ == "__main__":
    app.run(debug=True)


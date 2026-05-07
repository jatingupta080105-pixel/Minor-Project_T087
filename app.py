from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [
            float(request.form['Pregnancies']),
            float(request.form['Glucose']),
            float(request.form['BloodPressure']),
            float(request.form['SkinThickness']),
            float(request.form['Insulin']),
            float(request.form['BMI']),
            float(request.form['DPF']),
            float(request.form['Age'])
        ]

        final_input = np.array([features])

        prediction = model.predict(final_input)[0]

        result = "Diabetic" if prediction == 1 else "Not Diabetic"

        return render_template("result.html", prediction=result)

    except:
        return "Error: Please enter valid numeric values"

if __name__ == "__main__":
    app.run(debug=True)
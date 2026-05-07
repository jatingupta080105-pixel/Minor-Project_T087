# Diabetes Prediction System

A Machine Learning based web application that predicts whether a person is diabetic or not using medical parameters such as glucose level, BMI, insulin, age, and blood pressure.

##  Project Overview

This project uses a Logistic Regression Machine Learning model trained on the Pima Indians Diabetes Dataset. The trained model is integrated with a Flask web application where users can enter patient health details and get instant diabetes prediction results.

---

#  Technologies Used

## Programming Language

* Python

## Libraries Used

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Flask
* Pickle

---

#  Machine Learning Algorithm

## Logistic Regression

Logistic Regression is a supervised machine learning algorithm used for binary classification problems.

In this project:

* 0 = Non-Diabetic
* 1 = Diabetic

---

#  Project Structure

```bash
project/
│
├── app.py
├── diabetes.csv
├── model.pkl
├── model.ipynb
│
├── templates/
│   ├── index.html
│   └── result.html
```

---

#  Features

* User-friendly web interface
* Predicts diabetes instantly
* Uses trained machine learning model
* Flask-based web application
* Simple and lightweight project

---

#  Dataset Features

The model predicts diabetes using the following medical parameters:

* Pregnancies
* Glucose
* Blood Pressure
* Skin Thickness
* Insulin
* BMI
* Diabetes Pedigree Function
* Age

---

#  Working Flow

```text
User Input → Flask Application → Machine Learning Model → Prediction Result
```

---

#  How to Run the Project

## Step 1: Clone the Repository

```bash
git clone <your-github-repo-link>
```

## Step 2: Open Project Folder

```bash
cd <project-folder-name>
```

## Step 3: Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn scikit-learn flask
```

## Step 4: Run Flask App

```bash
python app.py
```

## Step 5: Open Browser

```text
http://127.0.0.1:5000/
```

---

#  Output

The application takes user medical data as input and predicts:

* Diabetic
* Not Diabetic

---

#  Future Improvements

* Add advanced machine learning algorithms
* Improve UI/UX design
* Deploy application online
* Add prediction probability percentage
* Improve model accuracy

---

#  Learning Outcomes

Through this project, I learned:

* Machine Learning basics
* Logistic Regression
* Model training and prediction
* Flask web development
* Frontend and backend integration
* GitHub project management

---

#  Author

Prince Kumar Khatri
jatin gupta

---

#  Conclusion

This project demonstrates how Machine Learning can be integrated with web development to create a real-world healthcare prediction application. It provides a simple and effective way to predict diabetes risk using patient medical information.

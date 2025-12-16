# Calories-Burnt-Prediction-using-SVR
This project aims to predict the number of calories burnt during a workout based on biological and workout-related features. 


**📌 Project Overview**

This project aims to predict the number of calories burnt during a workout based on biological and workout-related features.  

The project covers the **complete Machine Learning pipeline**, starting from data exploration and preprocessing, 

passing through model training and evaluation, and ending with **deployment using Flask with an interactive UI**.

The model used is **Support Vector Regression (SVR)** with an RBF kernel, which performs exceptionally well due to the strong non-linear relationships in the data.

---

## 📊 Dataset Description

### Columns Description
| Column Name   | Description |
|--------------|------------|
| User_ID      | Unique identifier for each user |
| Gender       | Gender of the user (male / female) |
| Age          | Age of the user (years) |
| Height       | Height of the user (cm) |
| Weight       | Weight of the user (kg) |
| Duration     | Workout duration (minutes) |
| Heart_Rate   | Average heart rate during workout (bpm) |
| Body_Temp    | Body temperature during workout (°C) |
| Calories     | Calories burnt during the workout |

---

## 🎯 Problem Definition

- **Features**:  
  `User_ID, Age, Height, Weight, Gender, Duration, Heart_Rate, Body_Temp`

- **Target**:  
  `Calories`

---

## 🛠️ Steps Performed

### Data Loading 
- Load the dataset using pandas.

---

###  Data Cleaning
- Checked for null values and removed them.
- Checked for duplicate rows and removed them.
- Dropped the `User_ID` column as it has no predictive value.

---

## 🔍 Exploratory Data Analysis (EDA)

- Used:
  - `info()`
  - `describe()`
- Analyzed the **distribution of Calories** (right-skewed).
- Scatter plots between:
  - Each feature and `Calories`.
- Correlation matrix between all columns.
- Grouped data by **Gender** and visualized average calories using a bar plot.

---

## 🧪 Feature Engineering

- Converted `Gender` column:
  ```python
  male   → 1
  female → 0
using map().

---

## 🤖 Model Training

- After completing data cleaning, EDA, and feature engineering, the model training phase was performed as follows:
  ```python
  The dataset was divided into features (X) and target (y).
  The target variable is Calories, which represents the number of calories burned during a workout.
  All remaining columns were used as input features for the model.

---

## ✂️ Train–Test Split

- By Splitting Data: 
  ```python
  The data was split into training and testing sets.
  The training set was used to train the model.
  The testing set was kept unseen to evaluate the model’s generalization ability.
  This step helps ensure that the model is not memorizing the data and can perform well on new, unseen samples.

---

## ⚖️ Feature Scaling

- Using Standar Scaler (mean 0 , std = 1)
  ```python
  Feature scaling was applied using StandardScaler.
  The scaler was fitted only on the training data.
  The learned scaling parameters were then applied to both training and testing sets.

- This step is crucial for SVR because:
    ```python  
    SVR is sensitive to feature magnitudes.
    Scaling ensures all features contribute fairly to the model.

---

## 📈 Model Selection – Support Vector Regression (SVR)

- Support Vector Regression (SVR) was chosen because:
  ```python 
  The target variable (Calories) is continuous.
  The relationship between features and target is not strictly linear.
  The RBF (Gaussain) kernel was used to capture non-linear relationships.

- Initial hyperparameters:
  ```python
  kernel = 'rbf'
  C = 1.0
  epsilon = 0.1

---

## 🔍 Model Evaluation

- The model was evaluated using:
  ```python
  Mean Absolute Error (MAE): Measures the average absolute difference between predicted and actual calories.
  R² Score: Indicates how well the model explains the variance in the target variable.

- Initial Results:
  ```python
  MAE: 2.30
  R²: 0.99
  These results indicate a very strong predictive performance.
   
---

## 🧪 Overfitting Check (Train vs Test Error)

- To ensure the model was not overfitting:
- MAE was calculated on both:
  ```python
  Training data
  Testing data

- Results:
  ```python
  Train MAE: 2.29
  Test MAE: 2.30

- The close values indicate that the model generalizes well and is not overfitting.

---

## ⚙️ Hyperparameter Tuning

- The regularization parameter C was adjusted from 1.0 → 1.2.
- This allows the model to better balance:
  ```python
  Margin maximization
  Error penalty

- Tuned Results:
  ```python
  R²: 0.99
  Train MAE: 1.99
  Test MAE: 2.02

- Performance improved without introducing overfitting.

---

## 💾 Model Saving

- The trained SVR model and the fitted scaler were saved.
- This allows:
  ```python
  Reusing the model without retraining
  Consistent preprocessing during deployment

---

## 🚀 Deployment

- The project was deployed using Flask.
- A web application was built to:
  ```python
  Accept user inputs (biological and workout features)
  Apply the saved scaler
  Predict calories burned in real time

- An interactive UI was designed for ease of use.
- ScreenShot:
  
  <img width="522" height="645" alt="Screenshot 2025-12-16 231553" src="https://github.com/user-attachments/assets/63cdf361-6d69-4ba1-be0e-e0ca01610020" />


---

## 📌 Technologies Used

- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- Flask
- Joblib
- HTML, CSS, JavaScript


# Fraud_Detection
**📌 UPI Fraud Detection using Machine Learning**

📖 Project Overview

This project develops a machine learning-based fraud detection system for identifying fraudulent UPI (Unified Payments Interface) transactions. The project performs exploratory data analysis (EDA), feature engineering, handles class imbalance using SMOTE, compares multiple machine learning models, and improves model performance through Optuna-based hyperparameter optimization.

The objective is to help financial institutions and digital payment platforms detect suspicious transactions more accurately while minimizing false alarms.

🎯 Problem Statement

Online payment fraud has become increasingly common with the rapid growth of digital transactions. Traditional rule-based systems often struggle to identify evolving fraud patterns.

This project aims to build a predictive machine learning model capable of distinguishing between legitimate and fraudulent UPI transactions using historical transaction data.

🛠 Technologies Used
Python
Pandas
NumPy
Matplotlib
Plotly Express
Scikit-learn
XGBoost
Optuna
Imbalanced-learn (SMOTE)
Jupyter Notebook

📂 Project Workflow
Data Collection
        ↓
Data Cleaning
        ↓
Exploratory Data Analysis (EDA)
        ↓
Feature Engineering
        ↓
Train-Test Split
        ↓
SMOTE (Handle Class Imbalance)
        ↓
Model Training
        ↓
Hyperparameter Tuning using Optuna
        ↓
Model Evaluation
        ↓
Business Recommendations

📊 Exploratory Data Analysis

The dataset was analyzed to identify important transaction patterns and fraud characteristics.

The analysis included:

Transaction amount distribution
Transaction type analysis
Fraud class distribution
Platform-wise transaction analysis
Geographic fraud distribution
Operating system analysis
Correlation heatmap
Feature relationship analysis
🤖 Machine Learning Models

The following models were trained and evaluated:

Decision Tree Classifier
Random Forest Classifier
Gradient Boosting Classifier
XGBoost Classifier

Each model was evaluated using:

Accuracy
Precision
Recall
F1 Score
ROC-AUC Score
⚙ Hyperparameter Optimization

Instead of relying on default model parameters, Optuna was used to automatically search for optimal hyperparameter combinations.



Hyperparameters tuned include:

Decision Tree
max_depth
min_samples_split
min_samples_leaf
Random Forest
n_estimators
max_depth
min_samples_split
min_samples_leaf
Gradient Boosting
n_estimators
learning_rate
max_depth
min_samples_split
min_samples_leaf
XGBoost
n_estimators
learning_rate
max_depth
min_child_weight

📈 Model Performance
| Model             |   Accuracy |  Precision |     Recall |   F1 Score |    ROC-AUC |
| ----------------- | ---------: | ---------: | ---------: | ---------: | ---------: |
| Decision Tree     | **0.9308** | **0.8056** | **0.9355** | **0.8657** | **0.9490** |
| Random Forest     | **0.9308** | **0.8056** | **0.9355** | **0.8657** | **0.9417** |
| Gradient Boosting | **0.9462** | **0.8529** | **0.9355** | **0.8923** | **0.9273** |
| XGBoost           | **0.9385** | **0.8286** | **0.9355** | **0.8788** | **0.9352** |


💼 Business Recommendations

Based on the exploratory data analysis and model findings, the following recommendations can help strengthen fraud detection strategies:

Implement real-time transaction monitoring to detect suspicious transactions as they occur.
Prioritize monitoring of high-risk transaction patterns, such as unusual transaction frequencies, amounts, or behavioral anomalies identified during EDA.
Use machine learning models alongside existing rule-based systems to improve fraud detection accuracy.
Deploy risk-based authentication (additional verification for suspicious transactions rather than all transactions) to reduce user inconvenience.
Continuously retrain the fraud detection model with recent transaction data to adapt to emerging fraud patterns.
Conduct regular model performance evaluations to ensure detection quality remains high as fraud tactics evolve.
Educate users about phishing attacks, fake payment requests, and common UPI fraud techniques to reduce social engineering attacks.
Encourage collaboration between financial institutions and payment platforms for faster identification of emerging fraud patterns.
🚀 Future Improvements
Deploy the model using Streamlit for real-time fraud prediction.
Integrate explainable AI (SHAP or LIME) to interpret model predictions.
Explore deep learning approaches for fraud detection.
Enable continuous model retraining using new transaction data.
Build a real-time fraud detection API for payment platforms.

📌 Conclusion

This project demonstrates an end-to-end fraud detection pipeline using machine learning techniques. By combining thorough exploratory data analysis, feature engineering, SMOTE for handling class imbalance, multiple classification algorithms, and Optuna-based hyperparameter optimization, the system effectively identifies fraudulent UPI transactions. The project highlights the value of data-driven fraud prevention and provides practical recommendations that can support more secure digital payment ecosystems.

⭐ One suggestion

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![XGBoost](https://img.shields.io/badge/XGBoost-Optimized-green)
![Optuna](https://img.shields.io/badge/Optuna-Hyperparameter%20Tuning-purple)
![License](https://img.shields.io/badge/License-MIT-yellow)

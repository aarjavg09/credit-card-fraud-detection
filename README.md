# Credit Card Fraud Detection

A machine learning project to detect fraudulent credit card transactions using Random Forest Classifier.

## Live Demo
[Click here to try the app](#) 

## Project Overview
This project uses machine learning to identify fraudulent transactions from a dataset of 284,807 credit card transactions. Only 0.17% of transactions are fraudulent, making this a highly imbalanced classification problem.

## Dataset
- Source: Kaggle - Credit Card Fraud Detection
- Total Transactions: 284,807
- Fraud Transactions: 492 (0.17%)
- Normal Transactions: 284,315 (99.83%)
- Features: 30 (Time, V1-V28, Amount)

## Tech Stack
- Python
- Pandas & NumPy
- Matplotlib & Seaborn
- Scikit-learn
- Imbalanced-learn (SMOTE)
- Streamlit
- Pickle

## Project Steps
1. Exploratory Data Analysis (EDA)
2. Data Visualization
3. Handling Class Imbalance using SMOTE
4. Train Test Split (80/20)
5. Random Forest Classifier
6. Model Evaluation
7. Streamlit Web App

## Model Performance
- Accuracy: 99%
- Precision: 98%
- Recall: 99%
- F1 Score: 99%

## How to Run
1. Clone the repository
2. Install dependencies
3. Run the Streamlit app

## Installation
pip install -r requirements.txt
streamlit run app.py

## Results
- Successfully detected 99% of fraud transactions
- Handled class imbalance using SMOTE
- Deployed as interactive web application

## Author
Your Name

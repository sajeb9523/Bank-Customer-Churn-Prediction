# Predictive Modeling and Risk Scoring for Bank Customer Churn

## Overview

Customer churn is a major challenge in the banking industry, as losing customers directly impacts revenue, customer lifetime value, and long-term profitability. This project focuses on predicting customer churn using Machine Learning techniques and identifying the key factors that influence customer retention.

The objective is to build a predictive system that can classify customers as likely to stay or leave the bank, allowing organizations to take proactive retention measures.

---

## Problem Statement

Banks collect large amounts of customer data but often lack predictive systems capable of identifying customers at risk of leaving. This project uses historical customer information to predict churn and generate risk-based insights for better decision-making.

---

## Project Objectives

* Predict customer churn using Machine Learning.
* Identify the most influential churn drivers.
* Generate churn probability scores.
* Support proactive customer retention strategies.
* Compare the performance of multiple classification models.

---

## Dataset Information

**Dataset Size:** 10,000 Customer Records

### Features Used

* Credit Score
* Geography
* Gender
* Age
* Tenure
* Account Balance
* Number of Products
* Credit Card Status
* Active Membership Status
* Estimated Salary
* Churn Status (Target Variable)

**Target Variable:** Exited

* 0 → Customer Retained
* 1 → Customer Churned

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Google Colab

---

## Project Workflow

1. Data Collection and Loading
2. Data Cleaning and Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Model Development
6. Model Evaluation
7. Feature Importance Analysis
8. Churn Risk Scoring

---

## Exploratory Data Analysis

The following analyses were performed:

* Customer Churn Distribution
* Gender-Based Churn Analysis
* Geography-Based Churn Analysis
* Age Distribution Analysis
* Correlation Heatmap

Key observations:

* Approximately 20% of customers churned.
* Germany exhibited the highest churn rate.
* Older customers showed higher churn tendencies.
* Active customers were less likely to leave the bank.

---

## Machine Learning Models

### Logistic Regression

Accuracy Achieved: **80.70%**

### Random Forest Classifier

Accuracy Achieved: **86.45%**

The Random Forest model outperformed Logistic Regression and was selected as the final model.

---

## Feature Importance Analysis

The most influential factors affecting customer churn were:

1. Age
2. Estimated Salary
3. Credit Score
4. Account Balance
5. Number of Products
6. Tenure
7. Active Membership Status

---

## Results

| Model               | Accuracy |
| ------------------- | -------- |
| Logistic Regression | 80.70%   |
| Random Forest       | 86.45%   |

### Best Model

**Random Forest Classifier**

Final Accuracy: **86.45%**

---

## Business Impact

The developed solution can help banks:

* Identify high-risk customers.
* Improve customer retention strategies.
* Reduce customer acquisition costs.
* Enhance customer satisfaction.
* Support data-driven decision-making.

---

## Future Scope

* Real-Time Churn Prediction
* Streamlit Dashboard Deployment
* XGBoost Implementation
* SHAP-Based Explainability
* Cloud Integration
* Banking CRM Integration

---

## Author

**Sajeb**

MBA Student | Data Analytics & Business Intelligence Enthusiast

---

## Project Outcome

A machine learning-based customer churn prediction system was successfully developed and evaluated. The Random Forest model achieved an accuracy of **86.45%**, providing a reliable solution for identifying customers at risk of leaving the bank and supporting proactive retention strategies.

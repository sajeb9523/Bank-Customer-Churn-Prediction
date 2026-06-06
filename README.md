# Predictive Modeling and Risk Scoring for Bank Customer Churn

## Project Overview

Customer retention is one of the most critical challenges in the banking industry. Acquiring new customers is significantly more expensive than retaining existing ones, making customer churn prediction an essential business problem.

This project develops a Machine Learning-based customer churn prediction system that identifies customers who are likely to leave the bank. By analyzing customer demographics, account information, and behavioral attributes, the model helps organizations take proactive actions to improve customer retention and reduce revenue loss.

---

## Problem Statement

Banks generate large volumes of customer data but often struggle to identify customers at risk of leaving. The objective of this project is to build an intelligent predictive model capable of forecasting customer churn and supporting data-driven retention strategies.

---

## Objectives

* Predict customer churn using Machine Learning techniques.
* Identify the key factors influencing customer attrition.
* Compare the performance of multiple classification algorithms.
* Generate churn risk insights for business decision-making.
* Support customer retention and relationship management strategies.

---

## Dataset Information

The project uses a banking customer dataset containing 10,000 customer records and multiple demographic and financial attributes.

### Features

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

### Target Variable

**Exited**

* 0 = Customer Retained
* 1 = Customer Churned

---

## Technologies and Tools

* Python
* Google Colab
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Pickle
* Microsoft Word

---

## Project Workflow

1. Data Collection and Loading
2. Data Preprocessing
3. Missing Value Analysis
4. Feature Engineering
5. Exploratory Data Analysis (EDA)
6. Model Development
7. Model Evaluation
8. Feature Importance Analysis
9. Churn Risk Scoring
10. Business Recommendations

---

## Exploratory Data Analysis

Several visualizations were created to understand customer behavior and churn patterns:

* Customer Churn Distribution
* Gender-wise Churn Analysis
* Geography-wise Churn Analysis
* Age Distribution Analysis
* Correlation Heatmap

### Key Findings

* Approximately 20% of customers churned.
* Germany exhibited higher churn rates compared to other regions.
* Older customers were more likely to leave the bank.
* Active members showed lower churn tendencies.
* Customer demographics and account characteristics significantly influenced churn behavior.

---

## Machine Learning Models

### Logistic Regression

Accuracy Achieved: **80.70%**

### Random Forest Classifier

Accuracy Achieved: **86.45%**

The Random Forest model demonstrated superior predictive performance and was selected as the final model.

---

## Model Performance Comparison

| Model               | Accuracy |
| ------------------- | -------- |
| Logistic Regression | 80.70%   |
| Random Forest       | 86.45%   |

### Best Performing Model

**Random Forest Classifier**

Final Accuracy: **86.45%**

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

These variables contributed most significantly to the model's predictive capability.

---

## Business Impact

The developed solution can assist banks in:

* Identifying high-risk customers.
* Reducing customer attrition.
* Improving customer retention strategies.
* Enhancing customer satisfaction.
* Supporting data-driven business decisions.
* Increasing long-term profitability.

---

## Repository Structure

```text
Bank-Customer-Churn-Prediction
│
├── Customer_Churn_Prediction_Report.pdf
├── European_Bank.csv
├── churn_model.pkl
├── Customer_Churn_Prediction.ipynb
└── README.md
```

---

## Future Scope

Future enhancements may include:

* Real-time churn prediction systems.
* Streamlit dashboard deployment.
* Implementation of advanced algorithms such as XGBoost and LightGBM.
* Explainable AI using SHAP values.
* Cloud deployment and API integration.
* Integration with CRM platforms for automated retention strategies.

---

## Author

**Sajeb**

MBA Student | Finance Analytics 

---

## Conclusion

This project successfully developed a Machine Learning-based customer churn prediction system for the banking sector. Among the evaluated models, the Random Forest Classifier achieved the highest accuracy of **86.45%**, making it an effective solution for identifying customers at risk of leaving. The insights generated from this study can help organizations implement proactive retention strategies, improve customer relationships, and support strategic business decision-making.

import streamlit as st
import pickle
import pandas as pd

# Load Model
model = pickle.load(open("churn_model.pkl", "rb"))

# Page Title
st.title("🏦 Bank Customer Churn Prediction")

st.write("""
This application predicts whether a bank customer is likely to leave the bank
using a Machine Learning model trained on customer banking data.
""")

st.info("Model Accuracy: 86.45% (Random Forest)")

# Input Fields
credit_score = st.number_input("Credit Score", min_value=300, max_value=900, value=600)

age = st.number_input("Age", min_value=18, max_value=100, value=35)

tenure = st.number_input("Tenure", min_value=0, max_value=10, value=5)

balance = st.number_input("Balance", min_value=0.0, value=50000.0)

num_products = st.number_input("Number of Products", min_value=1, max_value=4, value=1)

has_card = st.selectbox("Has Credit Card", [0, 1])

active_member = st.selectbox("Is Active Member", [0, 1])

salary = st.number_input("Estimated Salary", min_value=0.0, value=50000.0)

geography_germany = st.selectbox("Germany", [0, 1])

geography_spain = st.selectbox("Spain", [0, 1])

gender_male = st.selectbox("Male", [0, 1])

# Prediction Button
if st.button("Predict Customer Churn"):

    data = pd.DataFrame([[
        credit_score,
        age,
        tenure,
        balance,
        num_products,
        has_card,
        active_member,
        salary,
        geography_germany,
        geography_spain,
        gender_male
    ]], columns=[
        'CreditScore',
        'Age',
        'Tenure',
        'Balance',
        'NumOfProducts',
        'HasCrCard',
        'IsActiveMember',
        'EstimatedSalary',
        'Geography_Germany',
        'Geography_Spain',
        'Gender_Male'
    ])

    prediction = model.predict(data)
    probability = model.predict_proba(data)[0][1]

    st.subheader("Prediction Result")

    st.metric(
        label="Churn Probability",
        value=f"{probability * 100:.2f}%"
    )

    if probability > 0.70:
        st.error("🔴 High Risk Customer")

        st.write("""
        Recommended Actions:
        - Offer loyalty rewards
        - Provide personalized support
        - Contact customer proactively
        """)

    elif probability > 0.40:
        st.warning("🟡 Medium Risk Customer")

        st.write("""
        Recommended Actions:
        - Monitor customer engagement
        - Send promotional offers
        """)

    else:
        st.success("🟢 Low Risk Customer")

        st.write("""
        Recommended Actions:
        - Maintain regular customer service
        - Continue engagement programs
        """)

    if prediction[0] == 1:
        st.error("Customer is likely to churn.")
    else:
        st.success("Customer is likely to stay.")

import streamlit as st
import pickle
import pandas as pd

# Load model
model = pickle.load(open("churn_model.pkl", "rb"))

st.title("🏦 Bank Customer Churn Prediction")

credit_score = st.number_input("Credit Score", 300, 900, 600)
age = st.number_input("Age", 18, 100, 35)
tenure = st.number_input("Tenure", 0, 10, 5)
balance = st.number_input("Balance", 0.0, 300000.0, 50000.0)
num_products = st.number_input("Number of Products", 1, 4, 1)
has_card = st.selectbox("Has Credit Card", [0, 1])
active_member = st.selectbox("Is Active Member", [0, 1])
salary = st.number_input("Estimated Salary", 0.0, 200000.0, 50000.0)

geography_germany = st.selectbox("Germany", [0, 1])
geography_spain = st.selectbox("Spain", [0, 1])
gender_male = st.selectbox("Male", [0, 1])

if st.button("Predict"):
    data = [[credit_score, age, tenure, balance, num_products,
             has_card, active_member, salary,
             geography_germany, geography_spain, gender_male]]

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("Customer is likely to churn.")
    else:
        st.success("Customer is likely to stay.")

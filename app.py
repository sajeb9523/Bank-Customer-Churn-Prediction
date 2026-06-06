st.title("🏦 Bank Customer Churn Prediction")

st.write("""
This application predicts whether a bank customer is likely to leave the bank
using a Machine Learning model trained on customer banking data.
""")

st.info("Model Accuracy: 86.45% (Random Forest)")
if st.button("Predict"):

    prediction = model.predict(data)
    probability = model.predict_proba(data)[0][1]

    st.subheader("Prediction Result")

    st.metric(
        label="Churn Probability",
        value=f"{probability*100:.2f}%"
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
        - Monitor engagement
        - Send promotional offers
        """)

    else:
        st.success("🟢 Low Risk Customer")

        st.write("""
        Recommended Actions:
        - Maintain regular customer service
        - Continue engagement programs
        """)
      

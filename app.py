import streamlit as st
import pandas as pd
import joblib

model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

st.title("📊 Student Performance Predictor")
st.write("Predict Math Score based on Reading and Writing Scores")

reading = st.slider("Reading Score", 0, 100, 70)
writing = st.slider("Writing Score", 0, 100, 70)

if st.button("Predict"):
    input_df = pd.DataFrame({'reading score': [reading], 'writing score': [writing]})
    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)[0]
    st.success(f"🎯 Predicted Math Score: {prediction:.2f}")


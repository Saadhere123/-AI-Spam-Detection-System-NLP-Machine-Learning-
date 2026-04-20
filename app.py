import streamlit as st
import joblib
import re

model = joblib.load("best_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")


def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    return text


st.title("📩 AI Spam Detector")
st.write("Enter a message and check if it's Spam or Ham")

user_input = st.text_area("Enter Message")

if st.button("Predict"):
    cleaned = clean_text(user_input)
    vector = vectorizer.transform([cleaned])
    prediction = model.predict(vector)[0]

    if prediction == "spam":
        st.error("🚨 This is SPAM")
    else:
        st.success("✅ This is HAM (Safe Message)")
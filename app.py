import streamlit as st
import pandas as pd
import google.generativeai as genai
from serpapi import GoogleSearch

st.title("🌱 Nilo Health Finder")

# This part checks if your keys are ready
if "GEMINI_API_KEY" not in st.secrets:
    st.error("Missing Gemini Key! Go to Settings > Secrets to add it.")
else:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    st.success("Gemini is ready!")

uploaded_file = st.file_uploader("Upload your leads", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Found your leads!")
    if st.button("Start AI Analysis"):
        st.write("Robot is thinking...")

import streamlit as st
import pandas as pd
import joblib

st.title("Personal Finance Coach")

# 1. File Uploader Component
uploaded = st.file_uploader("Upload your bank statement (.csv)", type="csv")

# 2. Financial Goal Checkboxes & Input Fields
goals = st.multiselect("Select your goal(s)",
    ["Pay off debt", "Save for a house", "Pay tuition", "Build emergency fund"])
custom_goal = st.text_input("Or type a custom goal")
target = st.number_input("Target savings amount ($)", min_value=0)
deadline = st.date_input("Goal deadline")

if uploaded is not None:
    df = pd.read_csv(uploaded)
    st.write("### Raw Uploaded Data Preview:")
    st.dataframe(df.head())

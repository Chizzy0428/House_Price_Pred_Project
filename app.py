import streamlit as st
import numpy as np
import pickle

# Load trained model
with open(r"model.pkl", "rb") as f:
    model = pickle.load(f)


st.title("🏠 House Price Prediction App")

st.write("Fill in the details below to predict the house price:")

# Numeric inputs
area = st.number_input("Area (sqft)", min_value=100, step=10)
bedrooms = st.number_input("Number of Bedrooms", min_value=1, step=1)
bathrooms = st.number_input("Number of Bathrooms", min_value=1, step=1)
stories = st.number_input("Number of Stories", min_value=1, step=1)
parking = st.number_input("Parking Spaces", min_value=0, step=1)

# Binary categorical inputs (yes/no)
mainroad = st.selectbox("Is the house on a main road?", ["yes", "no"])
guestroom = st.selectbox("Guest Room Available?", ["yes", "no"])
basement = st.selectbox("Has Basement?", ["yes", "no"])
hotwaterheating = st.selectbox("Hot Water Heating Available?", ["yes", "no"])
airconditioning = st.selectbox("Air Conditioning Available?", ["yes", "no"])
prefarea = st.selectbox("Is it a Preferred Area?", ["yes", "no"])

# Convert yes/no to 1/0
binary_map = {'yes': 1, 'no': 0}
input_data = np.array([[
    area,
    bedrooms,
    bathrooms,
    stories,
    binary_map[mainroad],
    binary_map[guestroom],
    binary_map[basement],
    binary_map[hotwaterheating],
    binary_map[airconditioning],
    parking,
    binary_map[prefarea]
]])

if st.button("Predict Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated House Price: ${prediction:,.2f}")

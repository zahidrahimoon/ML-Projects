import streamlit as st
import pandas as pd
import pickle as pk

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #121212;
            color: #ffffff;
        }

        .title {
            font-size: 48px;
            color: #000; 
            text-align: center;
            font-weight: bold;
            margin-top: 20px;
        }

        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #0e0e0e;
            color: white;
            text-align: center;
            padding: 10px;
        }

        .stButton button {
            background-color: #00f7ff;
            color: black;
            font-weight: bold;
            border-radius: 8px;
        }

        .stTextInput, .stSelectbox, .stNumberInput {
            border-radius: 8px;
        }

    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="title">🏠 House Price Prediction</div>', unsafe_allow_html=True)

# Load model and data
with open(r'C:\coding\housepredictionproject\House_prediction_model.pkl', 'rb') as file:
    model = pk.load(file)

data = pd.read_csv(r'C:\coding\housepredictionproject\Cleaned_data.csv')
locations = sorted(data['location'].unique())

# Inputs
st.subheader("Fill the details to predict house price:")
location = st.selectbox("📍 Location", locations)
total_sqft = st.number_input("🏗️ Total Area (sqft)", min_value=100)
bath = st.selectbox("🚿 Number of Bathrooms", [1, 2, 3, 4, 5])
balcony = st.selectbox("🌴 Number of Balconies", [0, 1, 2, 3])
price_per_sqft = st.number_input("💰 Price per Sqft", min_value=100.0, value=5000.0)
bedrooms = st.selectbox("🛏️ Number of Bedrooms (BHK)", [1, 2, 3, 4, 5])

# Button and prediction
if st.button("🔮 Predict Price"):
    input_df = pd.DataFrame([[location, total_sqft, bath, balcony, price_per_sqft, bedrooms]],
                            columns=['location', 'total_sqft', 'bath', 'balcony', 'price', 'bedrooms'])
    prediction = model.predict(input_df)
    st.success(f"🏡 Estimated Price: PK {round(prediction[0], 2)} Lakh")

# Footer
st.markdown("""
    <div class="footer">
        Made by Zahid Rahimoon| 2025
    </div>
""", unsafe_allow_html=True)

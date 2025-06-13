import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Load model and data
model = joblib.load('random_forest_model.pkl')
data = pd.read_csv("data/Dataset.csv")

st.set_page_config(page_title="Reservoir Outflow Predictor", layout="centered")

st.markdown(
    """
    <style>
    h1, h3, p {
        color: black !important;
    }
    button {
    background-color: grey !important;
    }
    button:hover {
    background-color: #ADD8E6 !important;
    }
    .stApp {
        background-image: url("https://upload.wikimedia.org/wikipedia/commons/1/1b/Bhakra_Dam_Aug_15_2008.JPG");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    .stMainBlockContainer{
    padding: 60px 40px 20px 40px;
    background-color: rgba(255, 255, 255, 0.5);
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("💧 Reservoir Outflow Predictor")




# Take inputs for all 5 features used in training
inflow = st.number_input("Inflow (m³/s)", min_value=0.0)
evaporation = st.number_input("Evaporation (mm)")
reservoir_level = st.number_input("Reservoir Level (m)", min_value=0.0)
reservoir_stroage = st.number_input("Reservoir Storage (m)", min_value=0.0)


input_features = [[inflow, evaporation, reservoir_level, reservoir_stroage]]

if st.button("Predict Outflow"):
    pred_outflow = model.predict(input_features)
    st.success(f"Predicted Outflow: **{pred_outflow[0]:.2f} m³/s**")

# Show sample data and scatter plot
st.subheader("📊 Dataset")
st.dataframe(data.head())



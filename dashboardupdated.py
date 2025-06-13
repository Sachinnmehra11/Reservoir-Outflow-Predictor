import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Load model and data once
model = joblib.load('random_forest_model.pkl')
data = pd.read_csv("data/Dataset.csv")

# Page config
st.set_page_config(page_title="Reservoir Outflow Predictor", layout="centered")

# Custom CSS with DTU logo and background styling
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://upload.wikimedia.org/wikipedia/commons/1/1b/Bhakra_Dam_Aug_15_2008.JPG");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    .stMainBlockContainer {
        padding: 60px 40px 20px 40px;
        background-color: rgba(255, 255, 255, 0.5);
        border-radius: 15px;
    }
    h1, h3, p {
        color: black !important;
    }
    button {
        background-color: grey !important;
    }
    button:hover {
        background-color: #ADD8E6 !important;
    }
    .css-18e3th9 {
        position: relative;
    }
    .dtu-logo {
        position: absolute;
        top: 15px;
        right: 20px;
        width: 100px;
        z-index: 100;
    }
    </style>
    <img class="dtu-logo" src="https://upload.wikimedia.org/wikipedia/en/thumb/3/3a/Dtu_logo.svg/1200px-Dtu_logo.svg.png" alt="DTU Logo">
    """,
    unsafe_allow_html=True
)

st.title("💧 Reservoir Outflow Predictor")

# Initialize session state for inputs
if 'inflow' not in st.session_state:
    st.session_state.inflow = 0.0
if 'evaporation' not in st.session_state:
    st.session_state.evaporation = 0.0
if 'reservoir_level' not in st.session_state:
    st.session_state.reservoir_level = 0.0
if 'reservoir_storage' not in st.session_state:
    st.session_state.reservoir_storage = 0.0

# Placeholder function for future focus shift
def focus_next_element(current_key):
    pass

# Input fields
col1, col2 = st.columns(2)
with col1:
    inflow = st.number_input("Inflow (m³/s)", format="%.2f",
                             key='inflow', help="Daily water inflow volume.",
                             on_change=focus_next_element, args=('inflow',))
    evaporation = st.number_input("Evaporation (mm)", min_value=-100.0, format="%.2f",
                                  key='evaporation', help="Daily evaporation (can be negative).",
                                  on_change=focus_next_element, args=('evaporation',))
with col2:
    reservoir_level = st.number_input("Reservoir Level (m)", min_value=0.0, format="%.2f",
                                      key='reservoir_level', help="Current water level.",
                                      on_change=focus_next_element, args=('reservoir_level',))
    reservoir_storage = st.number_input("Reservoir Storage (Million m³)", min_value=0.0, format="%.2f",
                                        key='reservoir_storage', help="Total water stored.",
                                        on_change=focus_next_element, args=('reservoir_storage',))

# Input validation
def inputs_valid():
    return (
        isinstance(inflow, (int, float)) and inflow >= 0 and
        isinstance(evaporation, (int, float)) and  # Can be negative
        isinstance(reservoir_level, (int, float)) and reservoir_level >= 0 and
        isinstance(reservoir_storage, (int, float)) and reservoir_storage >= 0
    )

input_ready = inputs_valid()

# Predict button
pred_clicked = st.button("Predict Outflow", disabled=not input_ready)

if pred_clicked and input_ready:
    input_features = [[inflow, evaporation, reservoir_level, reservoir_storage]]
    pred_outflow = model.predict(input_features)

    st.success(f"Predicted Outflow: **{pred_outflow[0]:,.2f} m³/s**")

    # Confidence range ±5%
    lower = pred_outflow[0] * 0.95
    upper = pred_outflow[0] * 1.05
    st.write(f"Estimated Range: {lower:,.2f} - {upper:,.2f} m³/s")

    # Prediction chart
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.bar(["Predicted Outflow"], [pred_outflow[0]], color='steelblue')
    ax.set_ylabel("Outflow (m³/s)")
    ax.set_ylim(0, max(pred_outflow[0]*1.2, 10))
    ax.set_title("Reservoir Outflow Prediction")
    ax.errorbar("Predicted Outflow", pred_outflow[0],
                yerr=[[pred_outflow[0] - lower], [upper - pred_outflow[0]]],
                fmt='o', color='red', capsize=10, label='±5% Confidence Interval')
    ax.legend()
    st.pyplot(fig)

# Sample dataset preview
st.subheader("📊 Sample Dataset")
st.dataframe(data.head())

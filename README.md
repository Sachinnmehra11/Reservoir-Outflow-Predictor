# 💧 Reservoir Outflow Predictor using Machine Learning

📘 **Final Year B.Tech Project – Delhi Technological University (DTU)**  
📅 **Duration:** Dec 2024 – May 2025  
👤 **Author:** Himanshu ([GitHub](https://github.com/Himanshu-1402) | [LinkedIn](https://linkedin.com/in/himanshu-saroha))

---

## 📌 Project Overview

This project uses **machine learning** to predict **daily reservoir outflow** based on hydrological parameters such as inflow, evaporation, reservoir level, and storage.  
It integrates both **analytical modeling** and a **Streamlit-based web app** to visualize and interact with predictions in real time.

---

## 🔍 Key Features

- ✅ Real-time outflow prediction using a trained **Random Forest** regression model  
- 📊 ±5% confidence interval estimation  
- 🧮 Multiple modeling approaches: **Monte Carlo**, **Group Method**, **Backpropagation**  
- 🎯 Clean and interactive **Streamlit dashboard** with DTU branding  
- 🧾 Data preview and visualizations  
- 📁 Easy-to-use modular project structure  

---

## 🛠 Tech Stack

- **Language**: Python  
- **Libraries**: Pandas, Scikit-learn, Matplotlib, Streamlit, NumPy  
- **Deployment**: Streamlit Web App  
- **Data Tools**: Excel, CSV  
- **Model**: Random Forest (joblib)

---

## 📂 Project Structure

Reservoir-Outflow-Predictor/
├── dashboard.py # Basic Streamlit app
├── dashboardupdated.py # Enhanced dashboard with charts & DTU branding
├── backpropagation.ipynb # Notebook implementing backpropagation
├── montecarlo.ipynb # Monte Carlo simulation for outflow
├── groupmethod.ipynb # GMDH-based prediction
├── optimized.ipynb # Tuned ML model evaluation
├── notebook.ipynb # General EDA and modeling
├── Dataset.csv / dataset.xlsx # Input hydrological dataset
├── OutputData.xlsx # Sample output predictions
├── random_forest_model.pkl # Trained Random Forest model
├── requirements.txt # Python dependencies (recommended)
├── README.md # Project documentation
└── .gitignore # Ignore unneeded files (e.g., .pyc, checkpoints)


---

## 🚀 How to Run Locally

```bash
# Step 1: Clone the repository
git clone https://github.com/Himanshu-1402/Reservoir-Outflow-Predictor.git
cd Reservoir-Outflow-Predictor

# Step 2: Install required packages
pip install -r requirements.txt

# Step 3: Run the Streamlit dashboard
streamlit run dashboardupdated.py

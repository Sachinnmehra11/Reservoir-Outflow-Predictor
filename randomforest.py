
# Import required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Load the Excel file into a DataFrame
data = pd.read_excel('./data/Dataset.xlsx', sheet_name='Dataset')

# Clean column names by stripping any extra spaces
data.columns = data.columns.str.strip()

# Print column names to check
print(data.columns)

# Select relevant columns for prediction
selected_columns = data[['INFLOW', 'RESERVOIR STORAGE', 'EVAPORATION', 'RESERVOIR LEVEL', 'RELEASE (OUTFLOW)']]

# Show the first few rows of the data to understand its structure
print(data.head())


# Features (X) and target variable (y)
X = data[['INFLOW', 'EVAPORATION', 'RESERVOIR LEVEL', 'RESERVOIR STORAGE']]  # independent variables
y = data['RELEASE (OUTFLOW)']  # dependent variable (target)

# Split the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Random Forest Regressor model
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the model
rf_model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = rf_model.predict(X_test)

# Evaluate the model performance
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print the evaluation metrics
print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")


# Save model
joblib.dump(rf_model, 'random_forest_model.pkl')
print("Model saved as random_forest_model.pkl")


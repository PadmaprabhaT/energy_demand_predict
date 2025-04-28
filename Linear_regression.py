import pandas as pd
import pickle
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load the data
data = pd.read_csv('data/cleaned_final_data.csv')

# Select features and target
X = data[['country', 'year']]
y = data['electricity_demand']

# One-hot encode the categorical 'country' column
X_encoded = pd.get_dummies(X, columns=['country'])

# Save the order of columns used for training
with open('model/country_columns.pkl', 'wb') as f:
    pickle.dump(X_encoded.columns.tolist(), f)

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluation metrics
print("Model Trained Successfully!")
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))

# Plot actual vs predicted
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.6, color='dodgerblue')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel("Actual Electricity Generation")
plt.ylabel("Predicted Electricity Generation")
plt.title("Actual vs Predicted Electricity Generation")
plt.grid(True)
plt.tight_layout()
plt.savefig('static/images/actual_vs_predicted.png')  # <-- save plot

plt.close()  


# Save the trained model
with open('model/energy_model.pkl', 'wb') as f:
    pickle.dump(model, f)

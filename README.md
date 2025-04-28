# Energy Demand Prediction

A simple Flask web application to predict future **energy demand** based on **country** and **year** using a trained **Linear Regression** model.

## Project Structure
- `templates/index.html` — Frontend page
- `static/` — CSS and JavaScript files
- `model/energy_model.pkl` — Trained Linear Regression model
- `model/country_columns.pkl` — Country encoding for prediction
- `data/cleaned_final_data.csv` — Dataset used for model training

## How to Run
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Start the Flask app:
   ```
   python app.py
   ```
3. Open your browser and go to:  
   ```
   http://127.0.0.1:5000/
   ```

## Features
- Select country and year to predict energy demand.
- Displays prediction result dynamically.
- Shows request processing steps.
- Clean and responsive UI.



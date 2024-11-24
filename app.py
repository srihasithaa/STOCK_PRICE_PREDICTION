from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import datetime

app = Flask(__name__)

# Load dataset
data = pd.read_csv('stock_data.csv')
data['Date'] = pd.to_datetime(data['Date'])
data['Year'] = data['Date'].dt.year
data['Month'] = data['Date'].dt.month
data['Day'] = data['Date'].dt.day

# Preparing features and target
X = data[['Year', 'Month', 'Day', 'Open', 'High', 'Low', 'Volume']]
y = data['Close']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Input from frontend
        year = int(request.form['year'])
        month = int(request.form['month'])
        day = int(request.form['day'])
        open_price = float(request.form['open_price'])
        high = float(request.form['high'])
        low = float(request.form['low'])
        volume = float(request.form['volume'])

        # Prepare input
        input_features = [[year, month, day, open_price, high, low, volume]]
        predicted_price = model.predict(input_features)[0]

        return jsonify({'predicted_price': predicted_price})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True)

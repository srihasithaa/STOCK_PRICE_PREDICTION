Stock Price Prediction Using Linear Regression
This project demonstrates how to use Linear Regression to predict the closing price of a stock based on historical trading data. The model is deployed as a web application using Flask, enabling users to input stock features and receive predicted closing prices in real-time.

Key Features
Data Preprocessing:

The dataset (stock_data.csv) is preprocessed to extract useful features like Year, Month, and Day from the Date column.
Independent variables include: Year, Month, Day, Open, High, Low, and Volume.
Target variable: Close.
Model Training:

A Linear Regression model is trained using scikit-learn to predict the Close price of the stock.
The dataset is split into training (80%) and testing (20%) subsets for evaluation.
Web Application:

Frontend: Users input stock details (e.g., Year, Month, Day, Open, High, Low, Volume) via a form.
Backend: Flask processes these inputs, predicts the closing price, and returns the result in JSON format.

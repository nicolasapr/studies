import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import datetime

def predicting_values(X, y):

    X = X.copy()
    X['date'] = pd.to_datetime(X['date']).apply(lambda x: x.toordinal())

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    test_predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, test_predictions)

    tomorrow = pd.DataFrame({'date': [datetime.datetime.now() + datetime.timedelta(days=1)]})
    tomorrow['date'] = tomorrow['date'].apply(lambda x: x.toordinal())
    tomorrow_prediction = model.predict(tomorrow)
    
    return tomorrow_prediction, mse

market_data = yf.download('^GSPC', 
                         start=(datetime.datetime.now() - datetime.timedelta(days=365)).strftime('%Y-%m-%d'),
                         end=datetime.datetime.now().strftime('%Y-%m-%d'))

training_data = market_data[['Open', 'High', 'Low', 'Close', 'Volume']]
training_data = training_data.rename(columns={
    'Open': 'open', 
    'High': 'high', 
    'Low': 'low', 
    'Close': 'close', 
    'Volume': 'volume'
})
training_data['date'] = training_data.index

X = training_data[['date']]
y = training_data[['open', 'high', 'low', 'close', 'volume']]

predictions, mse = predicting_values(X, y)

results = pd.DataFrame(predictions, 
                      columns=['open', 'high', 'low', 'close', 'volume'])
print("\nPredicted values for tomorrow:")
print(results)
print(f"\nMean Squared Error: {mse}")

results.to_csv('predicted_values.csv', index=False)
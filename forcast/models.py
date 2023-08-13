from django.db import models
from tensorflow.keras.models import load_model
import requests

model_path = "forcast/stock_predictor_model.h5"
model = load_model(model_path)


def get_alpha_vantage_data(symbol, api_key):
    endpoint = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
    response = requests.get(endpoint)
    return response.json()  

from urllib import request
from django.shortcuts import render
from .forms import StockSearchForm
from .models import get_alpha_vantage_data, model
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import datetime
import pandas as pd
import requests
import yfinance as yf
import datetime
import json

def forcast(request):
    if request.method == "POST":
        form = StockSearchForm(request.POST)
        if form.is_valid():
            symbol = form.cleaned_data['symbol']
            end_date = datetime.datetime.now().date()  # 오늘 날짜
            start_date = end_date - datetime.timedelta(days=2*365)  # 오늘로부터 약 2년 전 날짜
            data = get_yahoo_finance_data(symbol, start_date=start_date, end_date=end_date)

            features = data[['Close']]
            features.columns = ['Close']
            scaler = MinMaxScaler(feature_range=(0,1))
            scaled_data = scaler.fit_transform(features)

            # 미래 주가 예측
            future_days = 30
            predictions = [scaled_data[-1]]
            current_data = scaled_data[-60:].tolist()
            for _ in range(future_days):
                predicted_value = model.predict(np.array(current_data).reshape(1, 60, 1))
                current_data.append(predicted_value[0])
                current_data = current_data[1:]
                predictions.append(predicted_value[0])

            predictions = scaler.inverse_transform(np.array(predictions).reshape(-1, 1))
            
            # 오늘 날짜부터 시작하는 예측 날짜 설정
            predicted_dates = [(end_date + datetime.timedelta(days=i)).strftime("%Y-%m-%d") for i in range(1, future_days+1)]

            context = {
                'form': form,
            'predictions': zip(predicted_dates, predictions),
            'predicted_dates_json': json.dumps(predicted_dates),
            'predicted_prices_json': json.dumps([float(price[0]) for price in predictions])
            }
            return render(request, 'forcast/forcast.html', context)
    else:
        form = StockSearchForm()
    return render(request, 'forcast/forcast.html', {'form': form})

def get_yahoo_finance_data(symbol, start_date, end_date):
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    return stock_data




def get_alpha_vantage_data(symbol, api_key):
    endpoint = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
    response = requests.get(endpoint)
    json_data = response.json()

    if "Time Series (Daily)" not in json_data:
        return None  # API 응답에 오류가 있을 수 있으므로 None 반환

    # 날짜별 종가를 DataFrame으로 변환
    df = pd.DataFrame.from_dict(json_data["Time Series (Daily)"], orient='index').sort_index()
    return df
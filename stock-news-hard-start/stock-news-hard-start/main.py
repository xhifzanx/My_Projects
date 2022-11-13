import newsapi
import requests
from newsapi import NewsApiClient
import datetime as dt
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

my_news_api_key = "YOUR API KEY"
my_alphavintage_api_key = "YOUR API KEY"

now = dt.date
today = now.today()
today = str(today)

stock_parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "interval":"5min",
    "apikey":my_alphavintage_api_key,
}
news_parameters = {
    "q": COMPANY_NAME,
    "from": "2022-09-5",
    "apiKey": my_news_api_key,
}


response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
date_list = [value for (key, value) in data.items()]
yesterday = float(date_list[0]["4. close"])
preyesterday = float(date_list[1]["4. close"])

difference = yesterday - preyesterday
print(f"difference between today's and yesterday's closing stock price: {abs(difference)}")
percentage = abs(difference/yesterday * 100)
print(percentage)
if percentage >= 5:
    print("alert")


respond = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
respond.raise_for_status()
news_data = respond.json()
for i in range(0, 3):
    print(f"{i+1}: {news_data['articles'][i]['content']}")






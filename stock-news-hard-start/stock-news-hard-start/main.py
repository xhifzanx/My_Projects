import newsapi
import requests
from newsapi import NewsApiClient
import datetime as dt
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

my_news_api_key = "083eef31b22246d6b0d1de64cef68c2f"
my_alphavintage_api_key = "DZ2IMOKZ6K8K9F09"

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
    "from": "2022-08-13",
    "apiKey": my_news_api_key,
}

#'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'

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

#https://newsapi.org/v2/everything?q=tesla&from=2022-07-12&sortBy=publishedAt&apiKey=083eef31b22246d6b0d1de64cef68c2f

respond = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
respond.raise_for_status()
news_data = respond.json()
for i in range(0, 3):
    print(f"{i+1}: {news_data['articles'][i]['content']}")


## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


import pandas as pd
import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv(dotenv_path=".env")

my_number = os.getenv("my_number")
twilio_number = os.getenv("twilio_number")
twilio_account_sid = os.getenv("twilio_account_sid")
twilio_auth_token = os.getenv("twilio_auth_token")
STOCK = "TSLA"
COMPANY_NAME = "Tesla"
alpha_api_key = os.getenv("alpha_api_key")
vantage_url_api = 'https://www.alphavantage.co/query'
new_api_key = os.getenv("new_api_key")
news_url = "https://newsapi.org/v2/everything?"
func = "TIME_SERIES_DAILY"
number_of_news = 3

# Stocks part

parameters = {"function": func, "symbol": STOCK, "apikey": alpha_api_key}

resp = requests.get(url=vantage_url_api, params=parameters)
resp.raise_for_status()

data = resp.json()["Time Series (Daily)"]
df = pd.DataFrame(data)
df = df.transpose()["4. close"].sort_values()
df = df.reset_index()
df.rename(columns={'index': 'date', '4. close': 'close'}, inplace=True)
df["close"] = df["close"].astype("float64")
df["date"] = pd.to_datetime(df["date"])
df = df.set_index("date").sort_index()
df["pct_change"] = df["close"].pct_change() * 100

variation_today = round(df["pct_change"].tail(1).to_list()[0], 2)

var_sign = ""
if variation_today > 0:
    var_sign = "🔺"
else:
    var_sign = "🔻"

# if abs(variation_today) >= 1:
if True:
    # News part

    params = {"q": COMPANY_NAME, "apiKey": new_api_key, "searchIn": "title", "language": "en", "sortBy": "publishedAt"}

    resp = requests.get(url=news_url, params=params)
    resp.raise_for_status()

    info = resp.json()

    titles = ["title" + str(n) for n in range(0, number_of_news)]
    descriptions = ["description" + str(n) for n in range(0, number_of_news)]
    title_info = []
    desc_info = []

    for n in range(0, number_of_news):
        title_info.append(info["articles"][:number_of_news][n]["title"])
        desc_info.append(info["articles"][:number_of_news][n]["description"])

    # Twilio part.

    articles = [f"TESLA{var_sign + str(variation_today)}.\nTitle: {title_info[n]}." for n in range(0, number_of_news)]

    client = Client(twilio_account_sid, twilio_auth_token)

    for article in articles:
        print(article)
        client.messages.create(
            body=article,
            to=my_number,
            from_=twilio_number)

# \nbrief: {desc_info[n]}

# zip_title_iterator = zip(titles, title_info)
# zip_info_iterator = zip(descriptions, desc_info)
#
# news_titles = dict(zip_title_iterator)
# news_descriptions = dict(zip_info_iterator)

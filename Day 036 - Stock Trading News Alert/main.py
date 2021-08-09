import requests
from newsapi import NewsApiClient
import random
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
alphavantage_api = ""  # your key
account_sid = ""  # your account sid
auth_token = ""  # your token


parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": alphavantage_api
}
# call api
response = requests.get(
    "https://www.alphavantage.co/query", params=parameters)
response.raise_for_status()
data = response.json()

# last day data
last_refreshed_data = float(list(data["Time Series (Daily)"].items())[
    0][1]["4. close"])


# day before last day
day_before_last = float(
    list(data["Time Series (Daily)"].items())[1][1]["4. close"])

# comapre the 2 closing prices:
difference = round((last_refreshed_data - day_before_last), 2)
percentage = difference/last_refreshed_data*100


def get_news():
    newsapi = NewsApiClient(api_key='')  # your key

    all_articles = newsapi.get_everything(
        q=COMPANY_NAME, language='en')

    articles = all_articles["articles"][:3]
    random_article = random.choice(articles)
    return random_article


def send_sms():
    client = Client(account_sid, auth_token)
    if percentage < 0:
        head = f"TSLA: 🔻{round(percentage)}%"
    elif percentage > 0:
        head = f"TSLA: 🔺{round(percentage)}%"
    else:
        head = f"TSLA: {round(percentage)}%"
    title = get_news()['title']
    url = get_news()['url']
    message = client.messages \
        .create(
            body=f"{head}\n{title} \nREAD HERE:\n{url}",
            from_='',  # your twilio number
            to=''  # your phone number
        )
    print(message.status)


send_sms()

import requests
from bs4 import BeautifulSoup
import smtplib

EMAIL = "dannypython1@gmail.com"
PASSWORD = "642819375"
PRICE = 39.99

URL = "https://www.amazon.ca/Razer-Death-Adder-Essential-RZ01-02540100-R3U1/dp/B07F7T8J9P/ref=sr_1_11?dchild=1&keywords=mouse&qid=1629638554&sr=8-11"
header = {
    "Accept-Language": "en,ar;q=0.9,en-GB;q=0.8,fr;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
}

response = requests.get(url=URL, headers=header)
soup = BeautifulSoup(response.text, "html.parser")

data = soup.find(id="priceblock_ourprice").getText()
item_price = float(data.split('$')[1])

product_title = soup.find(id="productTitle").getText().strip("\n")

if item_price < PRICE:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(to_addrs=EMAIL, from_addr=EMAIL,
                            msg=f"Subject:Amazon Price Alert!\n{product_title} is now {data}\n{URL}")

import requests
from bs4 import BeautifulSoup

response = requests.get(r"https://www.theguardian.com/film/2019/sep/13/100-best-films-movies-of-the-21st-century")
website_data = response.text

soup = BeautifulSoup(website_data, "html.parser")
movies_name = [name.getText() for name in soup.select(selector="h2 strong")]
number = 1

with open("movies.txt", mode='w') as file:
    for movie in movies_name:
        file.write(f"{number} {movie}\n")
        number += 1

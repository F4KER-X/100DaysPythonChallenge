import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

URL = "https://www.billboard.com/charts/hot-100"
CLIENT_ID = ""
CLIENT_SECRET = ""

# get data from site
date = input("Which year do you want to travel to? type the date in this format YYYY-MM-DD")

response = requests.get(url=f"{URL}/{date}")
website_data = response.text

soup = BeautifulSoup(website_data, "html.parser")
data = [song.getText() for song in
        soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")]

# auth spotify app
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://google.com/",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]

# get the songs
song_uris = []
year = date.split("-")[0]
for song in data:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# create playlist and add songs
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist["id"], tracks=song_uris)

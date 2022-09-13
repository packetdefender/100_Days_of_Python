import pprint

from bs4 import BeautifulSoup as bs
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import requests

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=os.environ["YOUR_APP_CLIENT_ID"],
        client_secret=os.environ["YOUR_APP_CLIENT_SECRET"],
        redirect_uri=os.environ["YOUR_APP_REDIRECT_URI"],
        scope="playlist-read-private user-read-private playlist-modify-private",
        show_dialog=True,
        cache_path="token.txt"
    ))

pp = pprint.PrettyPrinter(width=41, compact=True)
######## Test data ########
# auth_user = sp.current_user()
# print(auth_user['display_name'])
# URL = f"https://billboard.com/charts/hot-100/2015-07-11"
# song_name = "Super2man"
# year = "2001"
###########################

# Have user input date they are looking for
date = input("Lets travel back in time!  Where do you want to travel back to?  The format to use is YYYY-MM-DD: ")
URL = f"https://billboard.com/charts/hot-100/{date}"

# Get Website and turn it into text form
response = requests.get(URL)
website_date = response.text

# Use BS4 to parse website data and pull back elemenets that we are looking for
soup = bs(website_date, "html.parser")
all_song_names = soup.select(selector="div ul li ul li h3")

# Take what is returned from BS4 and turn it into a list, stripping all the unneeded data.
# Also taking the year out of the date input and extrapulating just the year
song_names = [song_name.getText().strip() for song_name in all_song_names]
year = date[0:4]

# Iterating through song name and searching spotify API for the track and returning artist, song, spotify UUID for both
song_info = []
for song_name in song_names:
    q_test = sp.search(q=f'track:{song_name} year: {year}', type='track', limit=1)
    try:
        song_info.append({"artist": q_test['tracks']['items'][0]['album']['artists'][0]['name'],
                          "artist_uri": q_test['tracks']['items'][0]['album']['artists'][0]['uri'],
                          "album_name": q_test['tracks']['items'][0]['album']['name'],
                          "album_uri": q_test['tracks']['items'][0]['album']['uri'],
                          "song_name": q_test['tracks']['items'][0]['name'],
                          "song_uri": q_test['tracks']['items'][0]['uri'] }
                         )
    except IndexError:
        print(f"{song_name} does not exist")

# Create playlist
user_id = sp.me()['id']
sp.user_playlist_create(user_id, name=f"Billboard top 100 from {date}!", description="Billboard top 100 playlist "
                                                                                          "created via Python", public=False)
song_uri = [song['song_uri'] for song in song_info]

print(len(song_uri))
my_playlist = sp.current_user_playlists()['items'][0]['id']
sp.playlist_add_items(my_playlist, song_uri)




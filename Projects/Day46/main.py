from bs4 import BeautifulSoup
import requests
import re
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint


date_back = input("Which year would you like to travel to? Type the date in this format YYY-MM-DD: ")
print(date_back)

content = requests.get(f"https://www.billboard.com/charts/hot-100/{date_back}")
billboard_webpage = content.text


soup = BeautifulSoup(billboard_webpage, "html.parser")


output = soup.find_all(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")

year = date_back.split("-")[0]

billboard=[]
for music in output:
    hit = music.getText()
    hitt2 = hit.replace("\n", "")
    hitt = hitt2.replace("\t", "")
    billboard.append(hitt)

print(billboard)




#-----------------------------------------Spotify info--------------------------------------#
SPOTIPY_CLIENT_ID= "52b42e0b5a3b4810be156f7af074fbc7"
SPOTIPY_CLIENT_SECRET = "abdf61661c31448d8b3f2d64b73dd3b8"
URI_REDIRECT = "https://example.com/"


OAUTH_AUTHORIZE_URL= 'https://accounts.spotify.com/authorize'
OAUTH_AUTHORIZE_URL= 'https://accounts.spotify.com/authorize'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private", redirect_uri=URI_REDIRECT,
                                               client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET,
                                               show_dialog=True, cache_path="token.txt"))

user_id = sp.current_user()["id"]
print(user_id)


uri_tracks = []
for music in billboard:
    results = sp.search(q=f"track: {music} year:{year}", type="track")
    #print(results)
    try:
        uri = results["tracks"]["items"][0]["uri"]
        uri_tracks.append(uri)
    except IndexError:
        print(f"{music} doesn't exist in Spotify. Skipped.")


#print(uri_tracks)

my_playlist = sp.user_playlist_create(user=f"{user_id}", name=f"{date_back} Billboard 100", public=False, description="Top tracks from back in the day")
print(my_playlist["id"])
playlist_ID = my_playlist["id"]


for track in uri_tracks:
    music_track=[]
    x = track.split(":")[2]
    music_track.append(x)
    sp.playlist_add_items(playlist_id=playlist_ID, items=music_track)







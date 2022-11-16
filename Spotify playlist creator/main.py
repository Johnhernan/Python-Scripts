import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

SPOTIFY_ID = "foo"
SPOTIFY_SECRET = "foo"
BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"

if __name__ == "__main__":
    #billboard_time = input("Where would you like to travel enter in YYYY-MM-DD format")
    billboard_time = "2000-02-21"
    response = requests.get(f"{BILLBOARD_URL}{billboard_time}")
    billboard_page = response.text

    soup = BeautifulSoup(billboard_page, "html.parser")

    songs = soup.find_all(name="span", class_="chart-element__information__song")
    artist = soup.find_all(name="span", class_="chart-element__information__artist")

    billboard_song_titles = [tag.getText() for tag in songs[0:3]]
    billboard_artist = [tag.getText() for tag in artist[0:3]]

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private",
                                                   client_id=SPOTIFY_ID,
                                                   client_secret=SPOTIFY_SECRET,
                                                   redirect_uri="http://example.com",
                                                   cache_path=".cache"))
    user_id = sp.current_user()["id"]

    year = billboard_time.split("-")[0]
    uri_list = []
    for song in billboard_song_titles:

        results = sp.search(q="track:"+song +
                              " year:"+year,
                            type='track')
        pp = pprint.PrettyPrinter(indent=2)
        pp.pprint(results["tracks"]["items"])

        tracks_found = results["tracks"]["items"]
        for track in tracks_found:
            if song in track["name"]:
                # for artist in billboard_artist:
                if any(track["artists"][0]["name"] in a for a in billboard_artist):
                    uri_list.append(track["uri"])
                    break

    playlist = sp.user_playlist_create(user=user_id, name=f"{billboard_time} Billboard 100", public=False)

    sp.playlist_add_items(playlist_id=playlist["id"], items=uri_list)

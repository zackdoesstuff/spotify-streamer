import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time

# Spotify credentials
username = '0wiocje3ml6cle88ocubogdhn'
client_id = 'b348e8b24e9147649d6f3cb704f9f881'
client_secret = '619baf8d91834d39b358db1d8496de49'
redirect_uri = 'https://theweeknd.com'


# Authorization
scope = ['app-remote-control', 'user-library-modify', 'user-library-read', 'user-modify-playback-state', 'user-read-playback-state', 'user-read-currently-playing','streaming']
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(username=username, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))

#list of albums
albums_list_1 = ['4yP0hdKOZPNshxUOjY0cZj', '2nLOHgzXzwFEpl62zAgCEC', '2ODvWsOgouMbaA5xf0RkJe', '4qZBW3f2Q8y0k1A84d4iAO', '742eAldb4AJKLoPgJhGRE7', '0P3oVJBFOv3TDXlYRhGL7s', '2FgMWuwMeTgJArP2RF3upF', '3MP8mUHuQlYrGUkrEG4qpJ']
albums_list_2 = ['0ccEYmcKK8UKt5zZ0lGgJ7', '5Gm2XKBgnlzd6qTi7LE1z2', '7MUY0WxCmHcgEEeQNjoe8a']

import random

while True:
    start_time = time.time()
    while time.time() - start_time < 19.2 * 60 * 60:
        album_id = random.choice(albums_list_1)
        album_tracks = sp.album_tracks(album_id)
        for track in album_tracks['items']:
            sp.start_playback(uris=[track['uri']])
            time.sleep(sp.track(track['id'])['duration_ms'] / 1000)

    start_time = time.time()
    while time.time() - start_time < 4.8 * 60 * 60:
        album_id = random.choice(albums_list_2)
        album_tracks = sp.album_tracks(album_id)
        for track in album_tracks['items']:
            sp.start_playback(uris=[track['uri']])
            time.sleep(sp.track(track['id'])['duration_ms'] / 1000)


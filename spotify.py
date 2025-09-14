import spotipy
from spotipy.oauth2 import SpotifyOAuth
import secrets

sp = secrets.keys.sp

def play_song(song_name, artist_name=None, device_id=None):
    try: 
        query = ''
        
        if song_name:
            query += song_name
        
        if artist_name:
            query += f" artist:{artist_name}"

        results = sp.search(q=query, type="track", limit=1)
        tracks = results.get("tracks", {}).get("items", [])

        if tracks:
            track_uri = tracks[0]["uri"]
            sp.start_playback(uris=[track_uri], device_id=device_id)
        else:
            print(f"unable to find song: {song_name}")

    except PermissionError:
        print(f'unable to find {song_name}')

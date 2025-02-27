from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas as pd
import matplotlib.pyplot as plt
import re

# Set up Spotify API Credentials
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id='9361a8bdc64d4b9783f76b8deef8fb8b',  # Replace with your Client ID
    client_secret='f7e214c0703c42cc8bea9dd904b35efe'  # Replace with your Client Secret
))

# Full playlist URL (example: Top Hits)
playlist_url = "https://open.spotify.com/playlist/5muSk2zfQ3LI70S64jbrX7?si=yKQkZx5_SFWIAIqRDaOsoA"

# Extract playlist ID using regex
playlist_id_match = re.search(r'playlist/([a-zA-Z0-9]+)', playlist_url)
if playlist_id_match:
    playlist_id = playlist_id_match.group(1)
else:
    print("Invalid playlist URL. Please check the format.")
    exit()

# Fetch playlist details
playlist = sp.playlist(playlist_id)
playlist_name = playlist['name']
playlist_description = playlist['description']
playlist_owner = playlist['owner']['display_name']
playlist_tracks = playlist['tracks']['items']

# Extract track details
track_list = []
for item in playlist_tracks:
    track = item['track']
    track_list.append({
        'Track Name': track['name'],
        'Artist': ', '.join([artist['name'] for artist in track['artists']]),
        'Album': track['album']['name'],
        'Release Date': track['album']['release_date'],
        'Popularity': track['popularity'],
        'Duration (minutes)': track['duration_ms'] / 60000
    })

# Convert data to DataFrame
tracks_df = pd.DataFrame(track_list)

# Save data to CSV
tracks_df.to_csv('spotify_playlist_tracks.csv', index=False)


print(tracks_df)



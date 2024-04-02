import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Initialize Spotipy client
scope = "user-library-read playlist-modify-public"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

def search_tracks(query):
    """
    Search for tracks based on a query.
    """
    results = sp.search(q=query, limit=10)
    for idx, track in enumerate(results['tracks']['items']):
        print(f"{idx + 1}. {track['name']} - {', '.join([artist['name'] for artist in track['artists']])}")

def create_playlist(name, track_uris):
    """
    Create a new playlist with the given name and add tracks to it.
    """
    user_id = sp.me()['id']
    playlist = sp.user_playlist_create(user=user_id, name=name)
    sp.playlist_add_items(playlist_id=playlist['id'], items=track_uris)

# Example usage
if __name__ == "__main__":
    print("Welcome to the Spotify project!")

    # Search for tracks
    query = input("Enter a song name or artist: ")
    search_tracks(query)

    # Create a playlist
    playlist_name = input("Enter a name for your playlist: ")
    track_uris = [
        "spotify:track:4iJyoBOLtHqaGxP12qzhQI",  # Example track URI
        "spotify:track:3wrREuS0L68qhmLWj3kcQw"   # Another example track URI
    ]
    create_playlist(playlist_name, track_uris)

    print("Playlist created successfully!")

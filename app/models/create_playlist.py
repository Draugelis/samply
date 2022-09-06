from app.tools.spotify.create_playlist import create_playlist
from app.tools.spotify.add_tracks import add_tracks


def create_and_update_playlist(name, description, tracks, token):
    playlist_id = create_playlist(name, description, token)
    snapshot = add_tracks(playlist_id, tracks, token)

    return snapshot

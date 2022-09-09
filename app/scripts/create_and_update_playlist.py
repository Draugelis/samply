from app.tools.spotify.add_tracks import add_tracks
from app.tools.spotify.create_playlist import create_playlist
from app.tools.spotify.helpers import get_playlist_url


def create_and_update_playlist(name, description, tracks, token):
    playlist_id = create_playlist(name, description, token)
    add_tracks(playlist_id, tracks, token)

    playlist_data = {
        'name': name,
        'url': get_playlist_url(playlist_id)
    }
    return playlist_data

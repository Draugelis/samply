from app.tools.spotify.add_tracks import add_tracks
from app.tools.spotify.create_playlist import create_playlist


def create_and_update_playlist(name, description, tracks, token):
    try:
        playlist_id = create_playlist(name, description, token)
        add_tracks(playlist_id, tracks, token)
    except Exception:
        return {
            'status': 'ERROR',
            'error': 'Failed to create playlist'
        }

    playlist_data = {
        'status': 'OK',
        'name': name,
        'id': playlist_id
    }
    return playlist_data

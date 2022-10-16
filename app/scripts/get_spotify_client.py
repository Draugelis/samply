import os


def get_spotify_client():
    return {
        'spotify_client_id': os.environ.get('spotify_client_id')
    }

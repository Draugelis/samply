import json

import requests
from app import logger
from app.tools.spotify.config import base_url
from app.tools.spotify.get_user import get_user
from app.tools.spotify.helpers import get_headers


def create_playlist(name, description, token):
    """Function for creating playlist
    on Spotify

    Args:
        name (str): Playlist name
        description (str): Playlist description (optional)
        token (str): Spofity auth token

    Raises:
        RuntimeError: Raised if HTTP request fails

    Returns:
        str: Playlist id
    """
    logger.debug(f'Creating {name} playlist')

    user = get_user(token)
    playlist_url = base_url + '/users/' + user + '/playlists/'
    headers = get_headers(token)
    playload = json.dumps({
        'name': name,
        'description': description
    })
    response = requests.post(playlist_url, headers=headers, data=playload)

    if response.status_code != 201:
        logger.error(f'Failed to create a playlist. {response.status_code}')
        raise Exception('Failed to create a playlist')

    logger.info(f'Successfully created playlist {name}')
    playlist_id = response.json()['id']
    return playlist_id

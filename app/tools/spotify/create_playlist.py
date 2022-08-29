import json

import requests
from app.tools.logger import setup_logger
from app.tools.spotify.config import base_url
from app.tools.spotify.get_user import get_user
from app.tools.spotify.helpers import get_headers


def create_playlist(name, description, token):
    logger = setup_logger(__name__)
    logger.debug(f'Creating {name} playlist')

    user = get_user(token)
    playlist_url = base_url + '/user/' + user + '/playlists/'
    headers = get_headers(token)
    playload = json.dumps({
        'name': name,
        'description': description
    })
    response = requests.post(playlist_url, headers=headers, data=playload)

    if response.status_code != 201:
        logger.error(f'Failed to create a playlist. {response.status_code}')
        raise RuntimeError('Failed to create a playlist')

    logger.info(f'Successfully created playlist {name}')
    playlist_id = response.json()['id']
    return playlist_id

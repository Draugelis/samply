import json

import requests
from app import logger
from app.tools.spotify.config import base_url
from app.tools.spotify.helpers import get_headers


def add_tracks(playlist_id, tracks, token):
    """Function for adding tracks to playlist
    on Spotify.

    Args:
        playlist_id (str): Spotify playlist
        tracks (list): list of track Spotify URIs to add
        token (str): Spofity auth token

    Raises:
        RuntimeError: Raised if HTTP request fails

    Returns:
        str: Spotify playlist snapshot id
    """
    logger.debug('Adding tracks to playlist')

    playlist_url = base_url + '/playlists/' + playlist_id + '/tracks/'
    headers = get_headers(token)
    playload = json.dumps({
        'uris': tracks
    })
    response = requests.post(playlist_url, headers=headers, data=playload)

    if response.status_code != 201:
        logger.error(f'Failed to add tracks. {response.status_code}')
        raise Exception('Failed to create a playlist')

    logger.info(f'Successfully added tracks {tracks}')
    snapshot_id = response.json()['snapshot_id']
    return snapshot_id

import requests
from app.tools.spotify import logger
from app.tools.spotify.config import base_url
from app.tools.spotify.helpers import get_headers, parse_track


def get_track(track_id, token):
    """Function for getting Spotify track data

    Args:
        track_id (str): Spotify track id
        token (str): Spotify auth token

    Raises:
        RuntimeError: Raised if HTTP request fails

    Returns:
        dict: Track data
    """
    logger.debug(f'Getting track {track_id}')

    track_url = base_url + '/tracks/' + track_id
    headers = get_headers(token)
    response = requests.get(track_url, headers=headers)

    if not response.ok:
        logger.error(f'Failed to get track {track_id}')
        raise RuntimeError('Failed to get track')

    logger.info(f'Got track {track_id}')
    track_data = parse_track(response.json())

    return track_data

import requests
from app import logger
from app.tools.spotify.config import base_url
from app.tools.spotify.helpers import get_headers, parse_track


def search_track(track, token):
    """Function for searching track data using
    Spotify API search endpoint

    Args:
        track (str): Track to find
        token (str): Auth token for the request

    Raises:
        RuntimeError: Raised if HTTP request status code is not 200

    Returns:
        dict: Track data
    """
    logger.debug(f'Searching {track}')

    search_url = base_url + '/search/'
    headers = get_headers(token)
    params = {
        'q': track,
        'type': 'track',
    }
    response = requests.get(search_url, headers=headers, params=params)

    if not response.ok:
        logger.error(f'{track} search failed; Status: {response.status_code}')
        raise Exception('Track search failed')

    logger.info(f'{track} was found')
    track_data = parse_track(response.json()['tracks']['items'][0])

    return track_data

import requests
from app import logger
from app.tools.spotify.config import base_url
from app.tools.spotify.helpers import get_headers


def get_user(token):
    """Function for getting user id

    Args:
        token (str): Spofity auth token

    Raises:
        RuntimeError: Raised if HTTP request fails

    Returns:
        str: Spotify user id
    """
    logger.debug('Searching user id')

    user_url = base_url + '/me/'
    headers = get_headers(token)
    response = requests.get(user_url, headers=headers)

    if not response.ok:
        logger.error('User search failed')
        raise Exception('User search failed')

    logger.info('User found')
    return response.json()['id']

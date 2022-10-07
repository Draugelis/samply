import requests
from app import logger
from app.tools.whosampled.config import base_url, headers
from app.tools.whosampled.helpers import is_track_path
from bs4 import BeautifulSoup


def search_track(track):
    """Function for searching track page

    Args:
        track (str): track name

    Returns:
        str: path to track page
    """
    # Start logging
    logger.debug(f'Starting {track} search')
    # Request search page
    params = {
        'q': track
    }
    search_url = base_url + '/search/'
    response = requests.get(search_url, headers=headers, params=params)
    logger.info(f'{track} search finished. Status {response.status_code}')

    if not response.ok:
        logger.error('Search for %s failed.' % (track,))
        raise RuntimeError('Track search failed')

    soup = BeautifulSoup(response.text, 'html.parser')
    top_hit = soup.findAll('div', {'class': 'topHit'})

    if not top_hit:
        logger.warning('Track %s was not found.' % (track,))
        raise RuntimeError('Track was not found')

    track_path = top_hit[0].a['href']

    if not is_track_path(track_path):
        logger.warning('Track %s was not found.' % (track,))
        raise Exception('Track was not found')

    logger.info('Track %s was found. Path: %s' % (track, track_path,))
    return track_path

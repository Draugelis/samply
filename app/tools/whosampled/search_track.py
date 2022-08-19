import requests
from bs4 import BeautifulSoup

from app.tools.whosampled.config import headers, base_url
from app.tools.whosampled.exceptions import TrackSearchError
from app.tools.logger import setup_logger

def search_track(track):
    """Function for searching track page

    Args:
        track (str): track name

    Returns:
        str: path to track page
    """    
    # Start logging
    logger = setup_logger(__name__)
    logger.debug('Starting search for %s' % track)
    # Request search page
    params = {
        'q': track
    }
    search_url = base_url + '/search/'
    response = requests.get(search_url, headers=headers, params=params)
    logger.info('Search request for %s finished. Ended with status %d' % (track, response.status_code,))

    if response.ok: 
        # Scrapping search page
        soup = BeautifulSoup(response.text, 'html.parser')
        top_hit = soup.findAll('div', {'class': 'topHit'})
        # Checking if track was found
        if top_hit:
            # Path to track info page; Structure: /{artist}/{track_name}
            track_path = top_hit[0].a['href'] 
            logger.info('Track %s was found. Path: %s' % (track, track_path,))
            return track_path 
        else:
            logger.warning('Track %s was not found.' % (track,))
            raise TrackSearchError(404)
    else:
        logger.error('Search for %s failed.' % (track,))
        raise TrackSearchError(response.status_code)

import requests
from bs4 import BeautifulSoup

from app.tools.whosampled.config import headers, base_url
from app.tools.whosampled.helpers import path_to_full_name, find_soup_samples
from app.tools.whosampled.exceptions import SampleSearchError
from app.tools.logger import setup_logger

def search_samples(track_path):
    """Function for searching track samples 

    Args:
        track_path (str): path to track page

    Returns:
        dict: dictionary consisting from track and samples
    """    
    # Start logging
    track_name = path_to_full_name(track_path)
    logger = setup_logger(__name__)
    logger.debug('Starting sample search for %s' % (track_name,))
    # Request samples page 
    sample_url = base_url + track_path + 'samples/'
    response = requests.get(sample_url, headers=headers)
    logger.info('Request to %s samples page finished with status %d.' % (track_name, response.status_code,))
    # Check if /samplse/ page exists
    if response.ok:
        soup = BeautifulSoup(response.text,'html.parser')
        sample_list = find_soup_samples(soup)
        logger.info('Finished searching samples for %s. Samples found: %d; %s' % (track_name, len(sample_list), sample_list,))
        return {
            'track': track_name,
            'samples': sample_list
        }
    elif response.status_code == 404:
        """HTTP 404 is returned if track has 3 or less samples
        In that case samples will be found under {base_url + track_path} 
        """
        # Search track page
        track_url = base_url + track_path
        response = requests.get(track_url, headers=headers)
        logger.info('Request to %s track page finished with status %d.' % (track_url, response.status_code,))
        # Scrapping track page
        soup = BeautifulSoup(response.text,'html.parser')
        sample_soup = soup.findAll('section', {'class': ''})[0]
        sample_list = find_soup_samples(sample_soup)
        logger.info('Finished searching samples for %s. Samples found: %d; %s' % (track_name, len(sample_list), sample_list,))
        return {
            'track': track_name,
            'samples': sample_list
        }
    else:
        logger.error('Request to %s samples page failed.' % (track_name,))
        raise SampleSearchError(response.status_code)
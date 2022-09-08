import requests
from app import logger
from app.tools.whosampled.config import base_url, headers
from app.tools.whosampled.helpers import path_to_full_name, scrape_samples


def search_samples(track_path):
    """Function for searching track samples

    Args:
        track_path (str): path to track page

    Returns:
        dict: dictionary consisting from track and samples
    """
    # Start logging
    track_name = path_to_full_name(track_path)
    logger.debug(f'Search {track_name} samples')
    # Request samples page
    sample_url = base_url + track_path + 'samples/'
    response = requests.get(sample_url, headers=headers)
    logger.info(f'Requested {sample_url}; Status {response.status_code}')

    if not response.ok and response.status_code != 404:
        logger.error('Request to %s samples page failed.' % (track_name,))
        raise RuntimeError('Sample search failed')

    if response.status_code == 404:
        """HTTP 404 is returned if track has 3 or less samples
        In that case samples will be found under {base_url + track_path}
        """
        track_url = base_url + track_path
        response = requests.get(track_url, headers=headers)
        logger.info(f'Requested {track_url}; Status {response.status_code}.')

    sample_list = scrape_samples(response.text)
    logger.info(f'Samples found for {track_name}: {sample_list}')
    return {
        'track': track_name,
        'samples': sample_list
    }

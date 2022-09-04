from app.tools.spotify import logger
from app.tools.spotify.helpers import get_track_id
from app.tools.spotify.get_track import get_track
from app.tools.spotify.search_track import search_track


def find_track_data(query, token):
    """Function for handling track search
    based on the query. Added to support
    track query by Spotify URL or by name

    Args:
        query (str): Search query
        token (str): Spotify auth token

    Returns:
        dict: Track data
    """
    logger.debug(f'Trying to find {query}')

    track_id = get_track_id(query)
    if track_id:
        return get_track(track_id, token)
    return search_track(query, token)

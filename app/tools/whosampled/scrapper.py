
from app.tools.whosampled.search_track import search_track
from app.tools.whosampled.search_samples import search_samples
from app.tools.whosampled.exceptions import SampleSearchError
from app.tools.whosampled.exceptions import TrackSearchError

def scrapper(track):
    """Scrapper function for searching track samples from whosampled

    Args:
        track (str): track name

    Returns:
        dict: dictionary consisting from track and samples
    """      
    try: 
        track_path = search_track(track)
    except TrackSearchError as e:
        return None
    else:
        try:
            samples = search_samples(track_path)
        except SampleSearchError as e:
            return None
        else:
            return samples

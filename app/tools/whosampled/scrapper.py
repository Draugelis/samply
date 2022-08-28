from app.tools.whosampled.search_samples import search_samples
from app.tools.whosampled.search_track import search_track


def scrapper(track):
    """Scrapper function for searching track samples from whosampled

    Args:
        track (str): track name

    Returns:
        dict: dictionary consisting from track and samples
    """
    track_path = search_track(track)
    samples = search_samples(track_path)
    return samples

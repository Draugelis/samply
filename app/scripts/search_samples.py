from app.tools.whosampled.scrapper import scrapper
from app.tools.spotify.find_track_data import find_track_data
from app.tools.helpers import listify, clean_track_name


def collect_samples(track, token):
    try:
        track_data = find_track_data(track, token)
        clean_track_query = f'{track_data["artist"]} {clean_track_name(track_data["track"])}'  # noqa: E501
        samples = scrapper(clean_track_query)
    except Exception:
        return {
            'status': 'ERROR',
            'error': 'Failed to find track'
        }

    samples_spotify_data = []
    for sample in samples['samples']:
        try:
            samples_spotify_data.append(find_track_data(sample, token))
        except Exception:
            pass

    return {
        'status': 'OK',
        'track': track_data,
        'samples': samples_spotify_data
    }


def search_samples(tracks, token):
    tracks = listify(tracks)
    samples = [collect_samples(track, token) for track in tracks]

    return samples

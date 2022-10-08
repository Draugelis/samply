from app.tools.whosampled.scrapper import scrapper
from app.tools.spotify.find_track_data import find_track_data


def collect_samples(track, token):
    try:
        samples = scrapper(track)
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

    track_data = find_track_data(track, token)

    result = {
        'status': 'OK',
        'track': track_data,
        'samples': samples_spotify_data
    }
    return result


def search_samples(tracks, token):
    samples = []
    for track in tracks:
        samples.append(collect_samples(track, token))

    return samples

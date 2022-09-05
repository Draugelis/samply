from app.tools.whosampled.scrapper import scrapper
from app.tools.spotify.find_track_data import find_track_data


def search_samples(track, token):
    # track_name = f'{track_data["artist"]} - {track_data["track"]}'

    samples = scrapper(track)
    samples_spotify_data = []
    for sample in samples['samples']:
        samples_spotify_data.append(find_track_data(sample, token))

    track_data = find_track_data(track, token)

    result = {
        'track': track_data,
        'samples': samples_spotify_data
    }
    return result


def gather_samples(tracks, token):
    samples = []
    for track in tracks:
        samples.append(search_samples(track, token))

    return samples

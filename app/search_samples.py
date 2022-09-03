from flask import request
from flask import jsonify

from app import app
from app.tools.whosampled.scrapper import scrapper
from app.tools.spotify.find_track_data import find_track_data


def get_samples(track, token):
    track_data = find_track_data(track, token)
    track_name = f'{track_data["artist"]}-{track_data["track"]}'
    samples = scrapper(track_name)
    spotify_sample_data = []

    for sample in samples['samples']:
        spotify_data = find_track_data(sample, token)
        spotify_sample_data.append(spotify_data)

    result = {
        'track': track_data,
        'samples': spotify_sample_data
    }
    return jsonify(result)


@app.route('/samples/', methods=['POST'])
def search_samples():
    token = request.headers.get('X-Spotify')
    content = request.json
    track = content['track']
    samples = get_samples(track, token)

    return samples

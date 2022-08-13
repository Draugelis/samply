import json 

from flask import request
from flask import jsonify

from app import app
from app.tools.whoscrapped import WhoScrapped
from app.tools.spotify import Spotify

def get_samples(track, token):
    scrapper = WhoScrapped()
    spotify = Spotify(token)

    track_path = scrapper.search_track(track)
    samples = scrapper.search_samples(track_path)
    spotify_track_data = spotify.search_track(track)
    spotify_sample_data = []

    for sample in samples:
        spotify_data = spotify.search_track(sample['sample'])
        spotify_sample_data.append(spotify_data)

    result = {
        'track': spotify_track_data,
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



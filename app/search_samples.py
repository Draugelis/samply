import json 

from flask import request
from flask import jsonify

from app import app
from app.tools.whosampled.scrapper import scrapper
from app.tools.spotify import Spotify

def get_samples(track, token):
    spotify = Spotify(token)

    samples = scrapper(track)
    spotify_track_data = spotify.search_track(track)
    spotify_sample_data = []

    for sample in samples['samples']:
        spotify_data = spotify.search_track(sample)
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



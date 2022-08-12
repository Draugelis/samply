from flask import request
from flask import jsonify

from app import app
from app.tools.spotify import Spotify


@app.route('/spotify/', methods=['POST'])
def search_spotify():
    content = request.json
    token = request.headers.get('X-Spotify')
    track = content['track']

    spotify = Spotify(token)
    spotify_data = spotify.search_track(track)

    return jsonify(spotify_data)

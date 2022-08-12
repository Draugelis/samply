from flask import request
from flask import jsonify

from app import app
from app.tools.spotify import Spotify


@app.route('/playlist/', methods=['POST'])
def create_playlist():
    content = request.json
    token = request.headers.get('X-Spotify')
    name = content['name']
    description = content.get('description')
    tracks = content['tracks']

    spotify = Spotify(token)
    playlist_id = spotify.create_playlist(name, description)
    spotify_data = spotify.add_tracks(playlist_id, tracks)
    
    return jsonify(spotify_data)

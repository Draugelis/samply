from flask import request
from flask import jsonify

from app import app
from app.tools.spotify.create_playlist import create_playlist
from app.tools.spotify.add_tracks import add_tracks


@app.route('/playlist/', methods=['POST'])
def create_and_update_playlist():
    content = request.json
    token = request.headers.get('X-Spotify')
    name = content['name']
    description = content.get('description')
    tracks = content['tracks']

    playlist_id = create_playlist(name, description, token)
    spotify_data = add_tracks(playlist_id, tracks, token)

    return jsonify(spotify_data)

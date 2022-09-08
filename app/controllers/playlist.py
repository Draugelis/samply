from app import app
from app.scripts import create_and_update_playlist
from flask import jsonify, request


@app.route('/playlist/', methods=['POST'])
def create_playlist():
    token = request.headers.get('X-Spotify')
    content = request.json
    name = content['name']
    description = content.get('description')
    tracks = content['tracks']

    result = create_and_update_playlist(name, description, tracks, token)

    return jsonify(result)

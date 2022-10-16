from app import app
from app.scripts import get_spotify_client
from flask import jsonify


@app.route('/spotify_client/', methods=['GET'])
def spotify_client():
    result = get_spotify_client()
    return jsonify(result)

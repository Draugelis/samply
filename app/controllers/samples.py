from app import app
from app.scripts import search_samples
from app.tools.helpers import listify
from flask import jsonify, request


@app.route('/samples/', methods=['POST'])
def sample_search():
    token = request.headers.get('X-Spotify')
    content = request.json
    tracks = content['tracks']

    samples = search_samples(listify(tracks), token)

    return jsonify(samples)

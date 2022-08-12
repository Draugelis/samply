from flask import request
from flask import jsonify

from app import app
from app.tools.whoscrapped import WhoScrapped


@app.route('/sample/', methods=['POST'])
def search_samples():
    content = request.json
    track = content['track']
    
    scrapper = WhoScrapped()
    track_path = scrapper.search_track(track)
    samples = scrapper.search_samples(track_path)

    return jsonify(samples)



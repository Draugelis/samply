from app import app
from flask import render_template


@app.route('/spotify', methods=['GET'])
def spotify_callback():
    return render_template('spotify.html')

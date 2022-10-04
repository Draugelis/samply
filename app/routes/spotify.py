from app import app
from flask import make_response, request, redirect


@app.route('/spotify', methods=['GET'])
def spotify_callback():
    token = request.args.get('access_token')
    max_token_age = request.args.get('expires_in')

    if not token:
        return

    response = make_response((redirect('/', code=302)))
    response.set_cookie('X-Spotify', value=token, max_age=max_token_age)

    return response

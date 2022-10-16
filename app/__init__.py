from flask import Flask

app = Flask(__name__, static_url_path='/static')

from app.tools.logger import setup_logger # noqa

logger = setup_logger(__name__)

from app.controllers.playlist import create_playlist # noqa
from app.controllers.samples import sample_search # noqa
from app.controllers.spotify_client import spotify_client # noqa
from app.routes.index import index_page # noqa
from app.routes.spotify import spotify_callback # noqa

from flask import Flask

app = Flask(__name__)

from app.tools.logger import setup_logger

logger = setup_logger(__name__)

from app.controllers.playlist import create_playlist
from app.controllers.samples import sample_search

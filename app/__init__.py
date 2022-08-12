from flask import Flask

app = Flask(__name__)

from app.search_samples import search_samples
from app.search_spotify import search_spotify
from app.create_playlist import create_playlist
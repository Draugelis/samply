from flask import Flask

app = Flask(__name__)

from app.controllers.samples import sample_search
from app.create_playlist import create_playlist
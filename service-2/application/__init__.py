from flask import Flask
from os import getenv

app = Flask(__name__)
app.config['SECRET_KEY'] = 'eriaoyhert438&%$gyfgw874'

from application import routes
from flask import Flask
from os import getenv

app = Flask(__name__)
app.config['SECRET_KEY'] = 'saguh732faioh349^&3rhedo'

from application import routes
from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')

app.config['SECRET_KEY'] = 'jhisaogh485*^(£"HSFB8qhr873u78&84'

# getenv('SECRET_KEY')

db = SQLAlchemy(app)



from application import routes
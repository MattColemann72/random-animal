from flask import Flask
from os import getenv
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

#app.config['SQLACHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
app.config['SECRET_KEY'] = 'jhisaogh485*^(£"HSFB8qhr873u78&84'
#db = SQLAlchemy(app)
#getenv('SECRET_KEY')

from application import routes
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:crudapppass@34.105.192.173:3306/fantasyfootball'
#'sqlite:///data.db' #'mysql+pymysql://root:crudapppass@host/fantasyfootball' DB location
# app.config['SECRET_KEY'] = 'A SOOCRET KOO'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

from application import routes
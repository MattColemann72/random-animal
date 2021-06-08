from flask import Flask
from os import getenv

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@externalip:port/dbname'
#'sqlite:///data.db' # eg.. 'mysql+pymysql://root:crudapppass@host/fantasyfootball' DB location
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app = Flask(__name__)
app.config['SECRET_KEY'] = 'saguh73249^&3rhedo'
#app.config['SECRET_KEY'] = getenv('SECRET_KEY')

from application import routes
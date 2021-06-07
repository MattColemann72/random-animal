from flask import Flask

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@externalip:port/dbname'
#'sqlite:///data.db' # eg.. 'mysql+pymysql://root:crudapppass@host/fantasyfootball' DB location
app.config['SECRET_KEY'] = 'SuPeRSecretK3y'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from application import routes
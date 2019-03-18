from flask import Flask
from flask_sqlalchemy import SQLAlchemy


SECRET_KEY = 'Sup3r$3cretkey'

app = Flask(__name__)

app.config['SECRET_KEY'] = '\xee\xca\xb9.Q\xf7\xbd\xfe\xda|X\xfb\x93\x98\xdc\x15\x15(\x13z#D\xef\x1a\xb3'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:project1@localhost/project1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 

db = SQLAlchemy(app)

app.config.from_object(__name__)


from app import views

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DATABASE = "diviapp.db"
DATABASE_URI = "sqlite:///" + DATABASE

class Config(object):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(Config):
    DEBUG = True

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)
db.init_app(app)
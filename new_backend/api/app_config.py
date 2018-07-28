from flask import Flask

class Config(object):
    DEBUG = False

class DevConfig(Config):
    DEBUG = True

app = Flask(__name__)
app.config.from_object(DevConfig)

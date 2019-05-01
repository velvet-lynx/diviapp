import os

from flask import Flask
from flask_cors import CORS

# instantiate db
cors = CORS()


def create_app(script_info=None):
    # instantiate the app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    cors.init_app(app)

    # register Blueprints
    from project.api.lines import lines
    app.register_blueprint(lines)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app}

    return app

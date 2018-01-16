from flask_restless import APIManager
from models import Stop, Line
from app_config import db, app
import app_config

db.create_all()

manager = APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(Stop(), methods=['GET', 'DELETE', 'PUT'])
manager.create_api(Line(), methods=['GET', 'DELETE', 'PUT'])

if __name__ == "__main__":
    app.run(debug=True)


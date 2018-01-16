from app_config import db
from models import Line, Stop, Link

db.drop_all()
db.create_all()
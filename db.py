from sqlalchemy import create_engine
from models import Line, Stop, LineStop, Base
from _config import DATABASE_URI

engine = create_engine(DATABASE_URI)

Base.metadata.create_all(engine)
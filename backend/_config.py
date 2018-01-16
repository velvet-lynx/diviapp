from sqlalchemy import create_engine

DATABASE = "diviapp.db"
DATABASE_URI = "sqlite:///" + DATABASE

db = create_engine(DATABASE_URI)

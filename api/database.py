import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import *


DATABASE_URL = 'sqlite:///default.sqlite3?check_same_thread=false'

ECHO_LOG = False

engine = sqlalchemy.create_engine(DATABASE_URL, echo=ECHO_LOG)

Base.metadata.create_all(bind=engine)

SessionClass = sessionmaker(engine)
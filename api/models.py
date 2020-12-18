from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Binary
from uuid import uuid4
from sqlalchemy.orm import relationship

def generate_uuid():
    return str(uuid4())

Base = declarative_base()

class JankenSession(Base):
    __tablename__ = 'janken_session'
    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String(length=255), default="Unknown")
    latest_stage = Column(Integer, default=0)
    users = relationship('User', backref='janken_session')


class User(Base):
    __tablename__ = 'user'
    id = Column(String(length=255), primary_key=True, default=generate_uuid)
    name = Column(String(length=255), default="Unknown")
    is_host = Column(Boolean, default=False)
    janken_session_id = Column(Integer, ForeignKey('janken_session.id'))


class Result(Base):
    __tablename__ = 'result'
    id = Column(Integer, primary_key=True)
    session_id = Column(Integer, ForeignKey('janken_session.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    is_win = Column(Boolean, default=False)
    stage = Column(Integer, default=0)
    hand = Column(Integer)
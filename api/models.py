from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Binary
from uuid import uuid4
from sqlalchemy.orm import relationship

def generate_uuid():
    return str(uuid4())

Base = declarative_base()

class Room(Base):
    __tablename__ = 'room'
    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String(length=255), default="Unknown")
    latest_stage = Column(Integer, default=0)
    host_user_id = Column(String(length=255), ForeignKey('user.id'))
    users = relationship('User', foreign_keys='User.room_id')
    host_user = relationship('User', foreign_keys=host_user_id)


class User(Base):
    __tablename__ = 'user'
    id = Column(String(length=255), primary_key=True, default=generate_uuid)
    name = Column(String(length=255), default="Unknown")
    room_id = Column(String(length=255), ForeignKey('room.id'))


class Result(Base):
    __tablename__ = 'result'
    id = Column(Integer, primary_key=True)
    room_id = Column(String(length=256), ForeignKey('room.id'))
    user_id = Column(String(length=256), ForeignKey('user.id'))
    is_win = Column(Boolean, default=False)
    stage = Column(Integer, default=0)
    hand = Column(Integer)
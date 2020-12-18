from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Enum
from uuid import uuid4
from sqlalchemy.orm import relationship


Base = declarative_base()

class JankenSession(Base):
    __tablename__ = 'janken_session'
    id = Column(String(length=255), primary_key=True, default=str(uuid4()))
    name = Column(String(length=255), default="Unknown")
    latest_stage = Column(Integer, default=0)
    users = relationship('User', backref='janken_session')
    
    def toDict(self):
        return {
            id: self.id,
            name: self.name,
            latest_stage: self.latest_stage,
            client_sessions: self.client_sessions
        }


class User(Base):
    __tablename__ = 'user'
    id = Column(String(length=255), primary_key=True, default=str(uuid4()))
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
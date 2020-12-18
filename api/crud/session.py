from models import JankenSession, User
from database import SessionClass
from contextlib import contextmanager
import schema

@contextmanager
def session_manager(session):
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise

# Turn User.is_host to True
def user_to_host(db: SessionClass, user: User):
    with session_manager(db) as session:
        user = session.query(User).filter(User.id == user.id)
        user.is_host = True

# set User's session
def set_user_to_session(user: User, janken_session: JankenSession):
        user.janken_session = janken_session
        
# create User (just like a session)
def create_user(db: SessionClass, name):
    with session_manager(db) as session:
        user = User(name=name)
        session.new(user)
        return user

# create JankenSession
def create_session(db: SessionClass, user_name, session_name):
    with session_manager(db) as session:
        user = User(name=user_name)
        janken_session = JankenSession(name=session_name)
        session.add(user)
        session.add(janken_session)
        user.janken_session = janken_session
        return {
            'user': user,
            'janken_session': janken_session
        }

def join_session(db: SessionClass, user_name, session_id):
    with session_manager(db) as session:
        user = User(name=user_name)
        janken_session = session.query(JankenSession).filter(JankenSession.id == session_id).first()
        user.janken_session = janken_session
        return {
            'user': user,
            'janken_session': janken_session
        }
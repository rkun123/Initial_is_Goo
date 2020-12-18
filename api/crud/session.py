from models import Room, User
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

# set User's room
def set_user_to_room(user: User, room: Room):
        user.room = room
        
# create User (just like a session)
def create_user(db: SessionClass, name):
    with session_manager(db) as session:
        user = User(name=name)
        session.new(user)
        return user

# create Room
def create_room(db: SessionClass, user_name, room_name):
    with session_manager(db) as session:
        user = User(name=user_name)
        room = Room(name=room_name)
        session.add(user)
        session.add(room)
        user.room = room
        return {
            'user': user,
            'room': room
        }

def join_room(db: SessionClass, user_name, room_id):
    with session_manager(db) as session:
        user = User(name=user_name)
        room = session.query(Room).filter(Room.id == room_id).first()
        user.room = room
        return {
            'user': user,
            'room': room
        }
from models import Room, User
from database import SessionClass
from contextlib import contextmanager
import schema
from fastapi import HTTPException

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
        user = User(name=user_name, is_host=True)
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

def start_game(db: SessionClass, room_id, user_id):
    with session_manager(db) as session:
        if session.query(Room).filter(Room.id == room_id).count() != 0:
            room = session.query(Room).filter(Room.id == room_id).first()
        else:
            raise HTTPException(status_code=404)

        if session.query(User).filter(User.id == user_id, User.room_id == room.id).count() == 0:
            raise HTTPException(status_code=404)
        elif not session.query(User).filter(User.id == user_id, User.room_id == room.id).first().is_host:
            raise HTTPException(status_code=400)
        room.latest_stage += 1
        print()
        return {
            'stage': room.latest_stage
        }

# def post_result(db: SessionClass, room_id, user_id, user_result):
#     with session_manager(db) as session:
#         if session.



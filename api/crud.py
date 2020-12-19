from models import Room, User, Result
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
        room = Room(name=room_name)
        session.add(room)
        session.commit()
        user = User(name=user_name, room_id=room.id)
        session.add(user)
        session.commit()
        room.host_user_id = user.id
        session.commit()
        return {
            'user': user,
            'room': room
        }

def join_room(db: SessionClass, user_name, room_id):
    with session_manager(db) as session:
        room = session.query(Room).filter(Room.id == room_id).first()
        user = User(name=user_name, room_id=room.id)
        session.add(user)
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
        host_users = session.query(User).filter(User.id == user_id, User.room_id == room.id)
        if host_users.count() == 0:
            raise HTTPException(status_code=404)
        elif host_users.first() != room.host_user:
            raise HTTPException(status_code=400)
        room.latest_stage += 1
        return {
            'stage': room.latest_stage
        }

def post_result(db: SessionClass, room_id, user_id, user_hand):
    with session_manager(db) as session:
        if session.query(Room).filter(Room.id == room_id).count() != 0:
            room = session.query(Room).filter(Room.id == room_id).first()
        else:
            raise HTTPException(status_code=404)
        if user_id == room.host_user_id:
            result = Result(room_id=room.id, user_id=user_id, stage=room.latest_stage, hand=user_hand)
            session.add(result)
            # ここに保留を処理する記述を書く
        else:
            host_results = session.query(Result).filter(Result.user_id == room.host_user_id)
            if host_results.count() == 0:
                result = Result(room_id=room.id, user_id=user_id, stage=room.latest_stage, hand=user_hand)
                session.add(result)
            else:
                # ここに勝利判定文を書く
                result = Result(room_id=room.id, user_id=user_id, stage=room.latest_stage, hand=user_hand)
                session.add(result)
        return {
            'result': result
        }
            


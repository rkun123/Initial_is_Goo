from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse
from database import SessionClass
from crud import *
import schema

import json

router = APIRouter()

def get_db():
  try:
    session = SessionClass()
    yield session
  except:
    session.rollback()
    raise
  finally:
    session.close()


@router.get('/')
async def root(request: Request, db: SessionClass = Depends(get_db)):
  await request.state.sio.emit('message', {}, namespace='/event', room='')
  return JSONResponse({"message": "OK"})

@router.post('/room', response_model=schema.CreateRoomResponse)
async def create_room_handler(req: schema.CreateRoomRequest, db: SessionClass = Depends(get_db)):
  res = create_room(db, req.user_name, req.room_name)
  response = schema.CreateRoomResponse(user=res['user'], room=res['room'])
  return response

@router.post('/room/{room_id}', response_model=schema.JoinRoomResponse)
async def join_room_handler(req: schema.JoinRoomRequest, room_id: str, db: SessionClass = Depends(get_db)):
  res = join_room(db, req.user_name, room_id)
  response = schema.JoinRoomResponse(user=res['user'], room=res['room'])
  return response

@router.post('/room/{room_id}/start_game')
async def start_game_handler(req: schema.StartGameRequest, room_id: str, db: SessionClass = Depends(get_db)):
  return start_game(db, room_id, req.user_id)

# @router.post('/room/{room_id}/result')
# async def post_result_handler(req: schema.PostResult, room_id: str, db: SessionClass = Depends(get_db)):
#   return post_result(db, room_id, req.user_id, req.result)

from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse
from database import SessionClass
from crud.session import *
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
  return JSONResponse({"message": "OK"})

@router.post('/session', response_model=schema.CreateJankenSessionResponse)
async def create_session_handler(req: schema.CreateJankenSessionRequest, db: SessionClass = Depends(get_db)):
  res = create_session(db, req.user_name, req.session_name)
  response = schema.CreateJankenSessionResponse(user=res['user'], janken_session=res['janken_session'])
  return response

@router.post('/session/{session_id}', response_model=schema.JoinJankenSessionResponse)
async def join_session_handler(req: schema.JoinJankenSessionRequest, session_id: str, db: SessionClass = Depends(get_db)):
  res = join_session(db, req.user_name, session_id)
  response = schema.JoinJankenSessionResponse(user=res['user'], janken_session=res['janken_session'])
  return response
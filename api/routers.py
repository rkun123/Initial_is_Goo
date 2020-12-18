from fastapi import APIRouter, Depends
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
  finally:
    session.close()


@router.get('/')
async def root(db: SessionClass = Depends(get_db)):
  return JSONResponse({"message": "OK"})

@router.post('/session', response_model=schema.CreateJankenSessionResponse)
async def create_session_handler(req: schema.CreateJankenSessionReq, db: SessionClass = Depends(get_db)):
  print(req.user_name, req.session_name)
  data = create_session(db, req.user_name, req.session_name)
  response = schema.CreateJankenSessionResponse()
  response.user = data.user
  response.janken_session = data.janken_session
  return response
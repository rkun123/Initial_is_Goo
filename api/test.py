from fastapi.testclient import TestClient
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from requests.auth import HTTPBasicAuth
from hashlib import sha256
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from main import app
from routers import get_db
from models import *

import pytest

engine = create_engine('sqlite:///test.db', echo=True, connect_args={'check_same_thread': False})
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
SessionClass = sessionmaker(engine)
session = SessionClass()

c = TestClient(app)

def get_db_for_test():
  try:
    yield session
  finally:
    session.close()

app.dependency_overrides[get_db] = get_db_for_test


# セッション作成用
def create_session():
  response = c.post('/session', json={
    'user_name': 'test_user2',
    'session_name': 'test_session2'
  })
  if response.status_code is 200:
    return response.json().janken_session



# セッション作成
def test_create_session():
  response = c.post('/session', json={
    'user_name': 'test_user',
    'session_name': 'test_session'
  })
  response_body = response.json()
  assert response.status_code == 200
  assert response_body.user is not None
  assert response_body.janken_session is not None

# セッション参加
# 参加者のセッション参加時を想定したテスト
# 予め作成したjanken_sessionのidを用いて，セッションに参加する．
# レスポンスは，新たに作成される自分自身を示すUser
def test_join_session():
  janken_session_id = create_session().id
  response = c.get('/session/{}'.format(janken_session_id))
  assert response.status_code == 200
  assert response_body.user is not None
  assert response_body.janken_session is not None
  return response_body.user

# セッションに本番開始要求を送る
# この操作には，該当セッションのホストとしての認証が必要である
# 認証は，リクエスト時にAuthorizationヘッダーへBearer {session_id}という形式で設定する．
# サーバー側では，request.state.user_id
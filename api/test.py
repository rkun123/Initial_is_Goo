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
def create_room():
  response = c.post('/room', json={
    'user_name': 'test_user2',
    'room_name': 'test_room2'
  })
  if response.status_code is 200:
    return response.json()['room']



# セッション作成
def test_create_room():
  response = c.post('/room', json={
    'user_name': 'test_user',
    'room_name': 'test_room'
  })
  print(response)
  response_body = response.json()
  print(response_body)
  assert response.status_code == 200
  assert response_body['user']['name'] == 'test_user'
  assert response_body['room']['name'] == 'test_room'
  assert response_body['user']['room_id'] == response_body['room']['id']

# セッション参加
# 参加者のセッション参加時を想定したテスト
# 予め作成したroomのidを用いて，セッションに参加する．
# Request
# レスポンスは，新たに作成される自分自身を示すUser
def test_join_room():
  room_id = create_room()['id']
  
  print('room_id', room_id)
  response = c.post('/room/{}'.format(room_id), json={
    'user_name': 'test_user2',
  })
  print(response.json())
  response_body = response.json()
  print(response_body)
  assert response.status_code == 200
  assert response_body['user']['name'] == 'test_user2'
  assert response_body['room']['name'] == 'test_room2'
  assert response_body['user']['room_id'] == response_body['room']['id']

# セッションに本番開始要求を送る
# この操作には，該当セッションのホストとしての認証が必要である
# 認証は，リクエスト時にAuthorizationヘッダーへBearer {room_id}という形式で設定する．
# サーバー側では，request.state.user_idにuser_idが格納されるようmiddlewareを定義，設定している．

def test_start_game():
  room = create_room()
  response = c.post('/room/{}/start_game'.format(room['id']), json={
    'user_id': room['host_user']['id'],
  })
  print(response.json())
  response_body = response.json()
  print(response_body)
  assert response.status_code == 200
  assert response_body['stage'] == 1

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


# ルーム作成用
def create_room():
  response = c.post('/room', json={
    'user_name': 'test_user2',
    'room_name': 'test_room2'
  })
  if response.status_code is 200:
    return response.json()['room']

# ルーム作成
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

# ルーム参加
# 参加者のルーム参加時を想定したテスト
# 予め作成したroomのidを用いて，ルームに参加する．
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

# ルームに本番開始要求を送る
# この操作には，該当ルームのホストとしての認証が必要である
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

def test_post_result():
  room = create_room()
  user_join_res = c.post('/room/{}'.format(room['id']), json={
    'user_name': 'test_user3',
  })
  formatted_user_join_res = user_join_res.json()
  print(formatted_user_join_res)
  join_user = formatted_user_join_res['user']
  response_host = c.post('/room/{}/result'.format(room['id']), json={
    'user_id': room['host_user']['id'],
    'room_id': room['id'],
    'hand': 1
  })
  response_host_body = response_host.json()
  response_client = c.post('/room/{}/result'.format(room['id']), json={
    'user_id': join_user['id'],
    'room_id': room['id'],
    'hand': 2
  })
  response_client_body = response_client.json()
  assert response_host.status_code == 200
  assert response_host_body['user_id'] == room['host_user']['id']
  assert response_host_body['room_id'] == room['id']
  assert response_host_body['hand'] == 1
  assert response_client.status_code == 200
  assert response_client_body['user_id'] == join_user['id']
  assert response_client_body['room_id'] == room['id']
  assert response_client_body['is_win'] == True
  assert response_client_body['hand'] == 2
  assert response_host_body['stage'] == response_client_body['stage']


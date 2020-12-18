# Initial_is_Goo

## /api
### 環境構築
1. `python 3.7`以上をインストール
1. `pipenv`を利用しているので、`pip install pipenv`
1. `pipenv shell`で、pipenv環境に入る
1. `pipenv install`で、pipenvに入ってるパッケージを自動インストール

#### サーバー起動
`$ uvicorn main:sio_app`

#### テストの実行
`$ pytest test.py`
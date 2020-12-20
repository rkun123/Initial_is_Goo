from fastapi import FastAPI, Request, HTTPException
from starlette.websockets import WebSocketState
from fastapi.middleware.cors import CORSMiddleware
import schema
from typing import List
from fastapi_socketio import SocketManager
from socket_handlers import SocketHandlers

from routers import router

app = FastAPI()
socket_manager = SocketManager(app=app)

origins = [
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)

@app.middleware('http')
async def inject_user_id_into_request(request: Request, call_next):
    try:
        auth_header = request.headers['Authorization']
        if auth_header is not None:
            auth_header_array = auth_header.split(' ')
            if auth_header_array[0] == 'Bearer':
                request.state.user_id = auth_header_array[1]
            else:
                return HTTPException(400, "Type of Authorization Header is invalid.")

    except:
        pass
    response = await call_next(request)
    return response

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, data):
        for connection in self.active_connections:
            if connection.client_state == WebSocketState.CONNECTED:
                await connection.send_json(data)

websocket_manager = ConnectionManager()

@app.websocket("/websocket")
async def websocket_endpoint(websocket: WebSocket):
    await websocket_manager.connect(websocket)
    while True:
        print('pending')
        data = await websocket.receive_json()
        print(data)
        if data['event'] == 'new_hand':
            await websocket_manager.broadcast(data)

        # if data['event'] == 'new_hand':
            # await websocket.send_json(data=data['payload'])

@app.middleware('http')
async def inject_websocket(request: Request, call_next):
    request.state.websocket = websocket_manager
    response = await call_next(request)
    return response


socket_manager._sio.register_namespace(SocketHandlers('/'))

app.include_router(router)
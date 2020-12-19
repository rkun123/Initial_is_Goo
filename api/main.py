from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import schema
import socketio

from routers import router

app = FastAPI()

sio = socketio.AsyncServer()
sio_app = socketio.ASGIApp(sio, other_asgi_app=app)

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

@app.middleware('http')
async def inject_sio_server(request: Request, call_next):
    request.state.sio = sio
    response = await call_next(request)
    return response

# Socket.IO
# new hand state
@sio.on('new_hand')
async def handle_new_hand(sid, data: schema.HandleNewHandData):
    print('Handle new hand. user:', data.user_id, 'hand:', data.hand)
    sio.emit('new_hand', data)

app.include_router(router)
import schema
from main import socket_manager as socket

@socket.on('connect', namespace='/janken')
async def handle_connect(sid, data: schema.HandleNewHandData):
    print('Connected Socket.io')
    await socket.emit('Hello')

# new hand state
@socket.on('new_hand')
async def handle_new_hand(sid, data: schema.HandleNewHandData):
    print('Handle new hand. user:', data.user_id, 'hand:', data.hand)
    await socket.emit('new_hand', data) 
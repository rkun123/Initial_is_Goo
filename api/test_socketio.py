from socketio import Client
from time import sleep

c = Client()

c.connect('http://localhost:8000', socketio_path='/ws/socket.io', namespaces='/event')

@c.on('new_hand', namespace='/event')
def event(data):
    print('new_hand')
    print(data)

c.emit('new_hand', data={
    'user_id': 'hoge',
    'room_id': 'fuga',
    'hand': 1
}, namespace='/event')


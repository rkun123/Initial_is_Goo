import schema
from socketio import AsyncNamespace

print("test")
class SocketHandlers(AsyncNamespace):
    async def on_connect(self, sid, environ):
        print('Connected by sid: ', sid)
        pass

    async def on_disconnect(self, sid):
        pass

    async def on_new_hand(self, sid, data):
        print('New hand')
        new_hand = schema.NewHandData.parse_obj(data)
        await self.emit('new_hand', new_hand.dict(), room=new_hand.room_id)

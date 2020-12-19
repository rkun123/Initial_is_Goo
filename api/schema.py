from pydantic import BaseModel
from typing import Optional

class Room(BaseModel):
    id: str
    name: str
    latest_stage: str

    class Config:
        orm_mode = True

class User(BaseModel):
    id: str
    name: str
    is_host: bool

    class Config:
        orm_mode = True

class CreateRoomRequest(BaseModel):
    user_name: str
    room_name: str

class CreateRoomResponse(BaseModel):
    room: Optional[Room]
    user: Optional[User]

class JoinRoomRequest(BaseModel):
    user_name: str

class JoinRoomResponse(CreateRoomResponse):
    pass

class StartGameRequest(BaseModel):
    user_id: str

class NewHandData(BaseModel):
    user_id: str
    room_id: str
    hand: int
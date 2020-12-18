from pydantic import BaseModel
from typing import Optional

class JankenSession(BaseModel):
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

class CreateJankenSessionRequest(BaseModel):
    user_name: str
    session_name: str

class CreateJankenSessionResponse(BaseModel):
    janken_session: Optional[JankenSession]
    user: Optional[User]

class JoinJankenSessionRequest(BaseModel):
    user_name: str

class JoinJankenSessionResponse(CreateJankenSessionResponse):
    pass

class HandleNewHandData(BaseModel):
    user_id: str
    hand: int

from pydantic import BaseModel

class CreateJankenSessionReq(BaseModel):
    user_name: str
    session_name: str

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
    janken_session: JankenSession

    class Config:
        orm_mode = True

class CreateJankenSessionResponse(BaseModel):
    janken_session: JankenSession
    user: User

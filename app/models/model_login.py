from pydantic import BaseModel

class LoginModel(BaseModel):
    emai: str
    password: str
    
from pydantic import BaseModel

class UserModel(BaseModel):
    user_name: str
    email: str
    password: str
    
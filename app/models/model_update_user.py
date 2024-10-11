from pydantic import BaseModel
from typing import Optional

class UpdateUserModel(BaseModel):
    user_name: Optional[str]
    email: Optional[str]
    password: Optional[str]
    
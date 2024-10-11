from bson import ObjectId
from fastapi import APIRouter, HTTPException

from app.models.model_user import UserModel

from app.utils.db import get_database
from app.utils.security import hash_password

create_user_router = APIRouter()

@create_user_router.post("/users")
async def register_user(user: UserModel):
    db = await get_database()
    existing_user = await db.users.find_one({"email": user.email})
    
    if existing_user:
        raise HTTPException(status_code=400, detail="Usuario ya existe")
    
    user_data = {
        "_id": str(ObjectId()),
        "user_name": user.user_name,
        "email": user.email,
        "password": hash_password(user.password)     
    }
    
    if user_data:
        await db.users.insert_one(user_data)
        raise HTTPException(status_code=200, detail="Usuario creado exitosamente")
        
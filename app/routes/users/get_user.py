from fastapi import APIRouter, HTTPException
from app.utils.db import get_database

get_user_router = APIRouter()

@get_user_router.get("/users/{user_id}")
async def get_user(user_id: str):
    db = await get_database()
    
    user = await db.users.find_one({"_id": user_id})
    
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    return user
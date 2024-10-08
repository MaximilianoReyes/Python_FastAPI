from fastapi import APIRouter, HTTPException
from app.utils.db import get_database

delete_user_router = APIRouter()

@delete_user_router.delete("/users/{user_id}")
async def delete_user(user_id:str):
    db = await get_database()
    
    user = await db.users.find_one({"_id": user_id})
    
    if user:
        await db.users.delete_one({"_id": user_id})
        raise HTTPException(status_code=200, detail="Usuarios eliminado correctamente")
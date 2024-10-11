from fastapi import APIRouter

from app.utils.db import get_database

list_user_router = APIRouter()

@list_user_router.get("/users")
async def list_users():
    db = await get_database()
    users = await db.users.find().to_list(100)
    return users

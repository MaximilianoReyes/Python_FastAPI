from fastapi import APIRouter, HTTPException

from app.models.model_update_user import UpdateUserModel

from app.utils.db import get_database
from app.utils.security import hash_password

update_user_router = APIRouter()

@update_user_router.put("/user/{user_id}")
async def update_user(user_id: str, user: UpdateUserModel):
    db = await get_database()
    
    user_exist = await db.users.find_one({"_id": user_id})
    
    if user_exist is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    update_data = {}
    result = None
    
    if user.user_name:
        update_data["user_name"] = user.user_name
        
    if user.email:
        email_exist = await db.users.find_one({"email": user.email, "_id": {"$ne": user_id}})
        if email_exist:
            raise HTTPException(status_code=400, detail="Email en uso")
        update_data["email"] = user.email
        
    if user.password:
        update_data["password"] = hash_password(user.password)
        
    if update_data is None:
        raise HTTPException(status_code=400, detail="No hay modificaciones")
    
    result = await db.users.update_one({"_id": user_id}, {"$set": update_data})
    
    if result is None:
        raise HTTPException(status_code=500, detail="La actualización fallo")
    else:
        raise HTTPException(status_code=200, detail="Usuario actualizado correctamente")
    
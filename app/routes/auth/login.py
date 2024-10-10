from fastapi import APIRouter, HTTPException
from app.utils.db import get_database
from app.models.model_login import LoginModel
from app.utils.security import verify_password
from app.utils.jwt import generate_jwt

login_router = APIRouter()

@login_router.post("/login")
async def login(user: LoginModel):
    db = await get_database()
    
    user_exist = await db.users.find_one({"email": user.emai})
    
    if user_exist is None: 
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    if not verify_password(user.password, user_exist["password"]): 
        raise HTTPException(status_code=400, detail="Contraseña incorrecta")
    
    token = generate_jwt(user_exist)
    
    return {"status": 200, "token": token}
        
    
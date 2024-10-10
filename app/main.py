from fastapi import FastAPI
from app.utils.db import connect_db

from app.routes.users.create_user import create_user_router
from app.routes.users.list_user import list_user_router
from app.routes.users.get_user import get_user_router
from app.routes.users.update_user import update_user_router
from app.routes.users.delete_user import delete_user_router

from app.routes.auth.login import login_router

app = FastAPI()

connect_db()

app.include_router(login_router)

app.include_router(create_user_router) 
app.include_router(list_user_router)
app.include_router(get_user_router)
app.include_router(update_user_router)
app.include_router(delete_user_router)


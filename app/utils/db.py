from dotenv import load_dotenv
import os 
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

client = None

def connect_db():
    global client 
    mongo_uri = os.getenv("MONGO_URI")
    client = AsyncIOMotorClient(mongo_uri)
    print("Base de datos conectada...")
    
async def get_database():
    if client is None:
        raise RuntimeError("Base de datos no conectada...")
    return client.python_fastapi

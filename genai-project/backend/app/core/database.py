from pymongo import MongoClient
from app.core.config import Config

client = None
db = None

def init_db():
    global client, db
    client = MongoClient(Config.MONGO_URI)
    db = client[Config.DB_NAME]

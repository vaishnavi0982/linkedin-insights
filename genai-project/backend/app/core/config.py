import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGO_URI = os.getenv("MONGO_URI")
    DB_NAME = os.getenv("DB_NAME", "linkedin_insights")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

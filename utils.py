import asyncio
from datetime import datetime
from db import create, read_one,db
from bson import ObjectId
from firebase_admin import auth
from dotenv import load_dotenv
load_dotenv()
def check_user_exists_using_email(email):
    user = read_one(db,"users", {"email": email})
    if user:
        return user
    return None
def check_user_exist_using_id(id):
    user = read_one(db,"users", {"_id": ObjectId(id)})
    if user:
        return user
    return None
def create_notification(user_id, title,description,type):
    notification = {
        "user_id": ObjectId(user_id),
        "title": title,
        'description': description,
        'type': type,
        'created_at': datetime.now(),
        'is_read': False
    }
    create(db, "notifications", notification)



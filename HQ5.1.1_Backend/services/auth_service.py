# services/auth_service.py
"""
Service layer for authentication-related operations.
"""

import bcrypt
from pymongo import MongoClient
from configs.settings import AppConfig

client = MongoClient(AppConfig.DB_URI)
db = client[AppConfig.DB_NAME]

def register_user(data):
    username = data['username']
    password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
    role = data['role']

    if db.users.find_one({"username": username}):
        raise ValueError("User already exists")
    
    user = {
        "username": username,
        "password": password,
        "role": role,
        "approved": False
    }
    db.users.insert_one(user)
    return {"username": username, "role": role}

def login_user(data):
    username = data['username']
    password = data['password']
    user = db.users.find_one({"username": username})

    if not user or not bcrypt.checkpw(password.encode('utf-8'), user['password']):
        raise ValueError("Invalid username or password")
    
    if not user['approved']:
        raise ValueError("User not approved by Super Admin")

    return {"user_id": str(user['_id']), "role": user['role']}

def get_user_role(user_id):
    user = db.users.find_one({"_id": user_id})
    if not user:
        raise ValueError("User not found")
    return user['role']


def approve_user(username):
    user = db.users.find_one({"username": username})
    if not user:
        return {"error": f"User '{username}' not found."}, 404
    if user.get("approved"):
        return {"message": f"User '{username}' is already approved."}
    db.users.update_one({"username": username}, {"$set": {"approved": True}})
    return {"message": f"User '{username}' has been approved."}
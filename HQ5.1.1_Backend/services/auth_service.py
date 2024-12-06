# services/auth_service.py
"""
Service layer for authentication-related operations.
"""

import bcrypt
from pymongo import MongoClient
from configs.settings import AppConfig

client = MongoClient(AppConfig.DB_URI)
db = client[AppConfig.DB_NAME]
users_collection = db["users"]

from models.user_model import UserModel

def register_user(username, password, role):
    existing_user = UserModel.find_user_by_username(username)
    if existing_user:
        return {"message": f"User '{username}' already exists", "status": "error"}

    UserModel.create_user(username, password, role, status="pending")
    return {"message": f"User '{username}' registered successfully. Awaiting approval.", "status": "success"}

def approve_user_service(username):
    user = UserModel.find_user_by_username(username)
    if not user:
        return {"message": f"User '{username}' does not exist", "status": "error"}
    if user.get("status") == "active":
        return {"message": f"User '{username}' is already approved.", "status": "error"}

    UserModel.update_user_status(username, "active")
    return {"message": f"User '{username}' has been approved successfully.", "status": "success"}

def login_user(username, password):
    user = UserModel.find_user_by_username(username)
    if not user:
        return {"message": "Invalid username or password", "status": "error"}
    if user.get("status") == "pending":
        return {"message": "User not approved by Super Admin", "status": "error"}
    if user.get("status") == "suspended":
        return {"message": "User account is suspended", "status": "error"}

    # Password verification logic here...
    return {"message": "Login successful!", "status": "success", "role": user.get("role")}
  
    
def get_user_role(user_id):
    user = db.users.find_one({"_id": user_id})
    if not user:
        raise ValueError("User not found")
    return user['role']


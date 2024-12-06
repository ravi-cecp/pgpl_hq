# services/module_service.py
# UTC Timestamp: 2024-12-05 00:00
# Handles logic for retrieving visible modules based on roles.

from flask import jsonify
from models.module_model import Module
from models.user_model import User
from utils.db_utils import db

def get_all_modules():
    """
    Fetches all modules from the database.
    """
    try:
        modules = list(db.modules.find({}, {"_id": 0}))  # Exclude the MongoDB `_id` field
        return modules
    except Exception as e:
        print(f"Error fetching modules: {e}")
        return []
        
        


def get_modules_for_user(username):
    """
    Retrieves the list of modules accessible to a user based on their role.
    """
    # Fetch the user's role from the database
    user = db.users.find_one({"username": username})
    if not user:
        return {"error": "User not found"}

    # Fetch the role details from the database
    role = db.roles.find_one({"name": user["role"]})
    if not role or "modules" not in role:
        return {"error": "Role or module access not defined for the user"}

    # Return the list of modules
    return {
        "role": role["name"],
        "modules": role.get("modules", [])
    }

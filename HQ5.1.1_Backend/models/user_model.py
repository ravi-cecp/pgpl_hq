from pymongo import MongoClient
from configs.settings import AppConfig

# MongoDB connection setup
client = MongoClient(AppConfig.DB_URI)
db = client[AppConfig.DB_NAME]
users_collection = db["users"]

class UserModel:
    @staticmethod
    def create_user(username, password, role, status="pending"):
        user = {
            "username": username,
            "password": password,
            "role": role,
            "status": status,  # Default to "pending"
        }
        users_collection.insert_one(user)
        return user

    @staticmethod
    def find_user_by_username(username):
        return users_collection.find_one({"username": username})

    @staticmethod
    def update_user_status(username, status):
        return users_collection.update_one({"username": username}, {"$set": {"status": status}})

    @staticmethod
    def get_all_users():
        return list(users_collection.find({}, {"_id": 0, "password": 0}))

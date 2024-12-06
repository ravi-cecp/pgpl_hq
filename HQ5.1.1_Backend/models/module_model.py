# models/module_model.py
# UTC Timestamp: 2024-12-05 00:00
# Defines the schema for application modules.

from configs.database import db
from pymongo import MongoClient
from configs.settings import AppConfig

# MongoDB connection setup
client = MongoClient(AppConfig.DB_URI)
db = client[AppConfig.DB_NAME]

class Module:
    @staticmethod
    def get_all_modules():
        """
        Fetch all modules from the database.
        """
        return list(db.modules.find({}, {"_id": 0}))

    @staticmethod
    def insert_module(module):
        """
        Insert a new module into the database.
        """
        return db.modules.insert_one(module)
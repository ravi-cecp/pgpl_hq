# controllers/user_controller.py
"""
User-related routes for management and approval.
"""

from flask import Blueprint, jsonify, request
from models.user_model import UserModel
from services.user_service import UserService
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["hq_app"]

user_bp = Blueprint("user", __name__)

#user_model = UserModel(db)
#user_service = UserService(user_model)


@user_bp.route("/users", methods=["GET"])
def get_all_users():
    users = UserModel.get_all_users()
    return jsonify(users)

@user_bp.route("/users/approve/<user_id>", methods=["POST"])
def approve_user(user_id):
    result = user_service.approve_user(user_id)
    if result.modified_count:
        return jsonify({"message": "User approved"}), 200
    return jsonify({"error": "User not found"}), 404

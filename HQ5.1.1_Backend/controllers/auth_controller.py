# controllers/auth_controller.py
"""
Authentication-related routes.
"""

from flask import Blueprint, request, jsonify, session
from services.auth_service import register_user, login_user, get_user_role, approve_user_service
from utils.response_handler import success_response, error_response
from configs.settings import db

users_collection = db['users']  # Assuming 'users' is the collection name

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    role = data.get("role")

    if not username or not password or not role:
        return jsonify({"message": "Missing required fields", "status": "error"}), 400

    response = register_user(username, password, role)
    return jsonify(response)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"message": "Missing required fields", "status": "error"}), 400

    response = login_user(username, password)
    return jsonify(response)


@auth_bp.route("/approve", methods=["POST"])
def approve_user():
    data = request.get_json()
    username = data.get("username")

    if not username:
        return jsonify({"message": "Username is required", "status": "error"}), 400

    response = approve_user_service(username)
    return jsonify(response)


@auth_bp.route('/role', methods=['GET'])
def role():
    try:
        user_id = request.args.get('user_id')
        role = get_user_role(user_id)
        return success_response("User role fetched successfully", {"role": role})
    except Exception as e:
        return error_response(str(e))


@auth_bp.route('/logout', methods=['POST'])
def logout_user():
    # Clear the user's session
    session.clear()
    return jsonify({"message": "User logged out successfully"}), 200

@auth_bp.route('/user', methods=['GET'])
def get_user():
    """
    Retrieve user details by username.

    Query Params:
        username (str): The username to fetch details for.

    Returns:
        dict: User details or an error message.
    """
    username = request.args.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400

    user = users_collection.find_one({"username": username}, {"_id": 0, "password": 0})  # Exclude sensitive fields
    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify({"status": "success", "user": user}), 200


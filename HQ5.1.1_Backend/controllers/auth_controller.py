# controllers/auth_controller.py
"""
Authentication-related routes.
"""

from flask import Blueprint, request, jsonify
from services.auth_service import register_user, login_user, get_user_role
from utils.response_handler import success_response, error_response

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        result = register_user(data)
        return success_response("User registered successfully", result)
    except Exception as e:
        return error_response(str(e))

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        result = login_user(data)
        return success_response("Login successful", result)
    except Exception as e:
        return error_response(str(e))

@auth_bp.route('/role', methods=['GET'])
def role():
    try:
        user_id = request.args.get('user_id')
        role = get_user_role(user_id)
        return success_response("User role fetched successfully", {"role": role})
    except Exception as e:
        return error_response(str(e))

@auth_bp.route('/approve', methods=['POST'])
def approve_user():
    try:
        data = request.get_json()
        username = data.get('username')
        if not username:
            return jsonify({"error": "Username is required"}), 400
        response = approve_user_service(username)  # Call the function from auth_service
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
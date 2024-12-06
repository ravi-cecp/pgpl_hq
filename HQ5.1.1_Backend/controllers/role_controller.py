# controllers/role_controller.py
# UTC Timestamp: 2024-12-05 00:00
# Handles role creation and management.

from flask import Blueprint, request, jsonify, session
from services.role_service import create_roles_and_users
from models.role_model import Role

role_bp = Blueprint('role', __name__)

@role_bp.route('/init', methods=['POST'])
def initialize_roles():
    """Endpoint to initialize roles and users."""
    create_roles_and_users()
    return jsonify({"message": "Roles initialized successfully"}), 200


@role_bp.route('/list', methods=['GET'])
def list_roles():
    """Endpoint to list all roles."""
    roles = Role.get_all_roles()
    return jsonify({"roles": roles}), 200
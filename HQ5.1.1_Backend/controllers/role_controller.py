# controllers/role_controller.py
# UTC Timestamp: 2024-12-05 00:00
# Handles role creation and management.

from flask import Blueprint
from services.role_service import create_roles_and_users

role_bp = Blueprint('role', __name__)

@role_bp.route('/initialize', methods=['POST'])
def initialize_roles():
    create_roles_and_users()
    return {'message': 'Roles and dummy users initialized successfully'}
# End of role_controller.py

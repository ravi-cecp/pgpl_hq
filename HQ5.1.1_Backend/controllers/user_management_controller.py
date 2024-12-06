# controllers/user_management_controller.py
# UTC Timestamp: 2024-12-05 00:00
# Handles user approvals and listing.

from flask import Blueprint, request
from services.user_service import approve_user, list_pending_users

user_mgmt_bp = Blueprint('user_mgmt', __name__)

@user_mgmt_bp.route('/approve', methods=['POST'])
def approve_user_endpoint():
    user_id = request.get_json().get('user_id')
    return approve_user(user_id)

@user_mgmt_bp.route('/pending', methods=['GET'])
def pending_users():
    return list_pending_users()
# End of user_management_controller.py

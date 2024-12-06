# controllers/module_controller.py
# UTC Timestamp: 2024-12-05 00:00
# Handles visibility of modules based on user roles.

from flask import Blueprint, request
from services.module_service import get_modules_for_user

module_bp = Blueprint('module', __name__)

@module_bp.route('/visible', methods=['GET'])
def visible_modules():
    user_id = request.args.get('user_id')
    return get_modules_for_user(user_id)
# End of module_controller.py

# services/module_service.py
# UTC Timestamp: 2024-12-05 00:00
# Handles logic for retrieving visible modules based on roles.

from flask import jsonify
from models.module_model import Module
from models.user_model import User

def get_modules_for_user(user_id):
    user = User.objects(id=user_id).first()
    if not user:
        return jsonify({'error': 'User not found'}), 404

    if not user.approved:
        return jsonify({'error': 'User is not approved'}), 403

    modules = Module.objects(roles_allowed=user.role)
    module_list = [{'id': str(module.id), 'name': module.name, 'description': module.description} for module in modules]
    return jsonify({'modules': module_list}), 200
# End of module_service.py

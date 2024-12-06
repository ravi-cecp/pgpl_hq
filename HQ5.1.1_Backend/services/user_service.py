# services/user_service.py
"""
Service layer for user-related operations.
"""

class UserService:
    def __init__(self, user_model):
        self.user_model = user_model

    def get_all_users(self):
        return self.user_model.get_all_users()

    def approve_user(self, user_id):
        return self.user_model.update_user(user_id, {"approved": True})

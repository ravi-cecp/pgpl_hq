# utils/validators.py
# UTC Timestamp: 2024-12-05 00:00
# Input validation functions.

def validate_username(username):
    if not username or len(username) < 3:
        return False, "Username must be at least 3 characters long."
    return True, None

def validate_password(password):
    if not password or len(password) < 6:
        return False, "Password must be at least 6 characters long."
    return True, None
# End of validators.py

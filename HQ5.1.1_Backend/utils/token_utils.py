# UTC Timestamp: <insert UTC timestamp here>
# File: utils/token_utils.py

import jwt
from datetime import datetime, timedelta
from configs.settings import SECRET_KEY

def generate_token(user_id, role):
    """
    Generates a JWT token for the user.
    """
    return jwt.encode(
        {'user_id': str(user_id), 'role': role, 'exp': datetime.utcnow() + timedelta(hours=24)},
        SECRET_KEY,
        algorithm='HS256'
    )

def decode_token(token):
    """
    Decodes a JWT token to extract user details.
    """
    return jwt.decode(token, SECRET_KEY, algorithms=['HS256'])

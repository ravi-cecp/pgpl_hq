# configs/settings.py

import os
from datetime import datetime

class AppConfig:
    """
    Configuration class for the application.

    This class defines environment-specific settings such as database URI,
    JWT keys, and secret keys. Defaults are provided for local development.
    """
   # Database Name
    # Used to specify which database the application will use
    DB_NAME = os.getenv("DB_NAME", "hq_database")
    
    # MongoDB connection URI
    # Default is set to connect to a local MongoDB server
    DB_URI = os.getenv("DB_URI", "mongodb://localhost:27017/hq_database")

 

    # Application Secret Key
    # Used for session management and general application security
    SECRET_KEY = os.getenv("SECRET_KEY", "random_secret_key_12345")

    # JWT (JSON Web Token) Secret Key
    # Used for signing and verifying JWT tokens
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "super_random_jwt_key_67890")

    # JWT Token Expiry Time
    # Specifies how long the JWT token will remain valid (in seconds)
    # Default is 1 hour (3600 seconds)
    JWT_EXPIRY_SECONDS = int(os.getenv("JWT_EXPIRY_SECONDS", 3600))

    @staticmethod
    def CURRENT_TIME():
        """
        Returns the current UTC time.

        This method is used for timestamping various operations,
        ensuring a uniform time format across the application.
        """
        return datetime.utcnow()

    # Debug Mode
    # Enables or disables debug mode for local development
    DEBUG = os.getenv("DEBUG", "True").lower() in ("true", "1", "t")

    # Logging Level
    # Default logging level is INFO
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

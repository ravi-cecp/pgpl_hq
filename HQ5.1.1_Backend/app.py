# app.py
"""
Main entry point for the HQ application backend.
"""

import os
from flask import Flask, jsonify, session
from flask_session import Session
from flask_cors import CORS
from pymongo import MongoClient
from controllers.auth_controller import auth_bp
from controllers.user_controller import user_bp
from controllers.role_controller import role_bp
from configs.settings import AppConfig
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(AppConfig)

# Configure session settings
app.config["SECRET_KEY"] = "your-secret-key"  # Replace with a secure key
app.config["SESSION_TYPE"] = "filesystem"  # Store sessions on the file system
Session(app)

# Enable Cross-Origin Resource Sharing (CORS)
CORS(app)

# Initialize MongoDB connection
client = MongoClient(app.config["DB_URI"])
db = client[app.config["DB_NAME"]]

# Register blueprints
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(user_bp, url_prefix="/user")
app.register_blueprint(role_bp, url_prefix='/role')


# Health Check Endpoint
@app.route("/", methods=["GET"])
def health_check():
    """
    Simple health check to ensure the app is running.
    """
    return jsonify({"message": "HQ Backend is running!"}), 200




def initialize_roles_and_super_admin():
    """
    Initializes the required roles and creates a default Super Admin user if not present.
    """
    roles_collection = db.roles
    users_collection = db.users

    # Check and create roles
    required_roles = ["Super Admin", "Admin", "Sales", "Sourcing", "Ops Head", "Logistics", "Finance"]
    for role in required_roles:
        if not roles_collection.find_one({"name": role}):
            roles_collection.insert_one({"name": role, "permissions": "all" if role == "Super Admin" else "limited"})

    # Check and create Super Admin user
    if not users_collection.find_one({"username": "superadmin"}):
        users_collection.insert_one({
            "username": "superadmin",
            "password": "123",  # Replace with a secure password
            "role": "Super Admin",
            "approved": True,  # Ensure this field is set
            "created_at": datetime.utcnow()
        })
        print("Super Admin user created successfully.")

# Initialize roles and Super Admin at startup
initialize_roles_and_super_admin()

@app.route("/")
def index():
    return {"message": "HQ Backend is running!"}

# Error Handlers
@app.errorhandler(404)
def not_found_error(error):
    """
    Handle 404 Not Found errors.
    """
    return jsonify({"error": "Not Found", "message": str(error)}), 404

@app.errorhandler(500)
def internal_server_error(error):
    """
    Handle 500 Internal Server errors.
    """
    return jsonify({"error": "Internal Server Error", "message": str(error)}), 500

print("App Configurations: ", app.config)

# Main entry point
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Default to port 5000
    app.run(host="0.0.0.0", port=port, debug=True)

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
from controllers.module_controller import module_bp
from configs.settings import AppConfig
from datetime import datetime
from utils.db_utils import db

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
app.register_blueprint(module_bp)


# Health Check Endpoint
@app.route("/", methods=["GET"])
def health_check():
    """
    Simple health check to ensure the app is running.
    """
    return jsonify({"message": "HQ Backend is running!"}), 200


def initialize_roles_modules_and_users():
    """
    Initializes the required roles, modules, and test users.
    Creates a default Super Admin user if not present.
    """
    roles_collection = db.roles
    modules_collection = db.modules
    users_collection = db.users

    # Define modules
    modules = [
        {"id": 1, "name": "Sales", "description": "Placeholder description for Sales module."},
        {"id": 2, "name": "Sourcing", "description": "Placeholder description for Sourcing module."},
        {"id": 3, "name": "Ops Head", "description": "Placeholder description for Ops Head module."},
        {"id": 4, "name": "Finance", "description": "Placeholder description for Finance module."},
        {"id": 5, "name": "Logistics", "description": "Placeholder description for Logistics module."},
        {"id": 6, "name": "Tech Admin", "description": "Placeholder description for Tech Admin module."},
        {"id": 7, "name": "App System", "description": "Placeholder description for App System module."},
        {"id": 8, "name": "Vault", "description": "Placeholder description for Vault module."},
    ]

    # Define roles and their access to modules
    roles = [
        {"name": "Super Admin", "modules": [module["name"] for module in modules], "description": "Placeholder description for Super Admin."},
        {"name": "Admin", "modules": [module["name"] for module in modules if module["name"] not in ["App System", "Vault"]], "description": "Placeholder description for Admin."},
        {"name": "Tech Admin", "modules": ["App System"], "description": "Placeholder description for Tech Admin."},
        {"name": "Sales", "modules": ["Sales"], "description": "Placeholder description for Sales."},
        {"name": "Sourcing", "modules": ["Sourcing"], "description": "Placeholder description for Sourcing."},
        {"name": "Ops Head", "modules": ["Sourcing", "Logistics"], "description": "Placeholder description for Ops Head."},
        {"name": "Finance", "modules": ["Finance"], "description": "Placeholder description for Finance."},
        {"name": "Logistics", "modules": ["Logistics"], "description": "Placeholder description for Logistics."},
    ]

    # Create test users for each role
    test_users = [
        {"username": f"{role['name'].replace(' ', '').lower()}_test", "password": "123", "email": "hq_test@daily.com", "role": role["name"], "approved": True, "status": "created and approved at app initialization", "created_at": datetime.utcnow()} 
        for role in roles
    ]

    # Insert modules if not already present
    existing_modules = list(modules_collection.find({}, {"_id": 0, "name": 1}))
    existing_module_names = {module['name'] for module in existing_modules}
    new_modules = [module for module in modules if module['name'] not in existing_module_names]
    if new_modules:
        modules_collection.insert_many(new_modules)
        print("Modules initialized.")

    # Insert roles if not already present
    existing_roles = list(roles_collection.find({}, {"_id": 0, "name": 1}))
    existing_role_names = {role['name'] for role in existing_roles}
    new_roles = [role for role in roles if role['name'] not in existing_role_names]
    if new_roles:
        roles_collection.insert_many(new_roles)
        print("Roles initialized.")

    # Insert Super Admin user if not already present
    if not users_collection.find_one({"username": "superadmin"}):
        users_collection.insert_one({
            "username": "superadmin",
            "password": "123",  # Replace with a secure password
            "email": "hq_test@daily.com",
            "role": "Super Admin",
            "approved": True,
            "status": "created and approved at app initialization",
            "created_at": datetime.utcnow()
        })
        print("Super Admin user created successfully.")

    # Insert test users if not already present
    existing_users = list(users_collection.find({}, {"_id": 0, "username": 1}))
    existing_usernames = {user['username'] for user in existing_users}
    new_users = [user for user in test_users if user['username'] not in existing_usernames]
    if new_users:
        users_collection.insert_many(new_users)
        print("Test users created successfully.")
    
    print("Roles, modules, and test users initialized successfully.")


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

# Initialize roles,  modules and users.
initialize_roles_modules_and_users()

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

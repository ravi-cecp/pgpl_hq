# app.py
"""
Main entry point for the HQ application backend.
"""

import os
from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from controllers.auth_controller import auth_bp
from controllers.user_controller import user_bp
from configs.settings import AppConfig

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(AppConfig)

# Enable Cross-Origin Resource Sharing (CORS)
CORS(app)

# Initialize MongoDB connection
client = MongoClient(app.config["DB_URI"])
db = client[app.config["DB_NAME"]]

# Register blueprints
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(user_bp, url_prefix="/user")

# Health Check Endpoint
@app.route("/", methods=["GET"])
def health_check():
    """
    Simple health check to ensure the app is running.
    """
    return jsonify({"message": "HQ Backend is running!"}), 200

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

# controllers/role_controller.py
# UTC Timestamp: 2024-12-05 00:00
# Handles role creation and management.

from flask import Blueprint, request, jsonify, session
from services.role_service import create_roles_and_users
from models.role_model import Role
from pymongo import MongoClient
#from app import db
client = MongoClient("mongodb://localhost:27017")
db = client["hq_database"]

role_bp = Blueprint('role', __name__)

@role_bp.route('/init', methods=['POST'])
def initialize_roles():
    """Endpoint to initialize roles and users."""
    create_roles_and_users()
    return jsonify({"message": "Roles initialized successfully"}), 200



    
@role_bp.route('/list', methods=['GET'])
def list_roles():
    #    Endpoint to list all roles.

    roles = list(db.roles.find({}, {"_id": 0})) # Fetch roles from the roles collection
    return jsonify({"roles": roles}), 200
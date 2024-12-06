# controllers/module_controller.py
# UTC Timestamp: 2024-12-05 00:00
# Handles visibility of modules based on user roles.

from flask import Blueprint, request, jsonify
from services.module_service import get_all_modules, get_modules_for_user
from pymongo import MongoClient

module_bp = Blueprint("modules", __name__, url_prefix="/modules")

client = MongoClient("mongodb://localhost:27017")
db = client["hq_database"]
# Dummy data for modules (can be replaced with database queries)

@module_bp.route("", methods=["GET"])
def list_modules():
    """
    Endpoint to list all modules.
    """
    try:
        modules = get_all_modules()
        return jsonify({"modules": modules}), 200
    except Exception as e:
        return jsonify({"error": "Failed to fetch modules", "details": str(e)}), 500

@module_bp.route("/user/<role_name>", methods=["GET"])
def list_modules_for_user(role_name):
    """
    Endpoint to list modules accessible to a specific role.
    """
    try:
        modules = get_modules_for_user(role_name)
        return jsonify({"role": role_name, "modules": modules}), 200
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 404
    except Exception as e:
        return jsonify({"error": "Failed to fetch modules for user", "details": str(e)}), 500
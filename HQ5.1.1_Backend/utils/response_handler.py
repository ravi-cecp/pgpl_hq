# utils/response_handler.py
# UTC Timestamp: 2024-12-05 00:00
# Helper functions to standardize responses.

from flask import jsonify

def success_response(message, data=None):
    response = {'status': 'success', 'message': message}
    if data:
        response['data'] = data
    return jsonify(response), 200

def error_response(error, status_code=400):
    return jsonify({'status': 'error', 'message': error}), status_code
# End of response_handler.py

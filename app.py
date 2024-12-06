
# UTC Timestamp: <insert UTC timestamp here>
# File: app.py

from flask import Flask
from controllers.auth_controller import auth_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix='/api/auth')

if __name__ == '__main__':
    app.run(debug=True)

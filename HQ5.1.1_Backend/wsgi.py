# WSGI entry point for deploying the backend application

# UTC Timestamp: <insert UTC timestamp here>
# File: wsgi.py

from app import app

if __name__ == '__main__':
    app.run()

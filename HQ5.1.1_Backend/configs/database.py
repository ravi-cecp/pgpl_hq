# configs/database.py
# UTC Timestamp: 2024-12-05 00:00
# MongoDB connection configuration.

from flask_pymongo import PyMongo

db = PyMongo()

def init_app(app):
    app.config['MONGO_URI'] = 'mongodb://localhost:27017/hq_database'
    db.init_app(app)
# End of database.py

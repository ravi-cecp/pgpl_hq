# models/role_model.py
# UTC Timestamp: 2024-12-05 00:00
# Defines the schema for roles in the application.

from configs.database import db

class Role(db.Document):
    name = db.StringField(required=True, unique=True)
    description = db.StringField()
# End of role_model.py

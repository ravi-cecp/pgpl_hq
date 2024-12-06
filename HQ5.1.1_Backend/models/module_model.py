# models/module_model.py
# UTC Timestamp: 2024-12-05 00:00
# Defines the schema for application modules.

from configs.database import db

class Module(db.Document):
    name = db.StringField(required=True, unique=True)
    description = db.StringField()
    roles_allowed = db.ListField(db.ReferenceField('Role'))
# End of module_model.py

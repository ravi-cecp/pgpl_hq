from configs.settings import db

class Role:
    def __init__(self, name, description=None):
        self.name = name
        self.permission = permission
        self.description = description

    @staticmethod
    def insert_role(data):
        """Insert a new role into the database."""
        db.roles.insert_one(data)

    @staticmethod
    def get_all_roles():
        """Retrieve all roles from the database."""
        return list(db.roles.find({}, {"_id": 0}))

    @staticmethod
    def find_role(name):
        """Find a specific role by name."""
        return db.roles.find_one({"name": name}, {"_id": 0})

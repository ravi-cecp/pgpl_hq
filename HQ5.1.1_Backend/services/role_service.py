# services/role_service.py
# UTC Timestamp: 2024-12-05 00:00
# Logic for roles and dummy user creation.

from models.role_model import Role
from models.user_model import User
from configs.database import db

def create_roles_and_users():
    roles = ['Super Admin', 'Admin', 'Sales', 'Sourcing', 'Ops Head', 'Logistics', 'Finance']
    for role_name in roles:
        existing_role = Role.query.filter_by(name=role_name).first()
        if not existing_role:
            new_role = Role(name=role_name)
            db.session.add(new_role)
            db.session.commit()

            dummy_user = User(username=f'{role_name.lower()}_dummy', password='dummy123', role=new_role)
            db.session.add(dummy_user)
            db.session.commit()
# End of role_service.py

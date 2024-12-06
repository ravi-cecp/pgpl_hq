# models/user_model.py

"""
Defines the User model for MongoDB using PyMongo.
"""

class UserModel:
    """
    Model class for User management.
    Handles user-related database operations.
    """

    def __init__(self, db):
        """
        Initialize the UserModel with a database connection.

        Args:
            db: The PyMongo database connection object.
        """
        self.collection = db["users"]

    def create_user(self, user_data):
        """
        Create a new user document in the database.

        Args:
            user_data (dict): Dictionary containing user information.
        
        Returns:
            Inserted ID of the new user document.
        """
        return self.collection.insert_one(user_data).inserted_id

    def find_user_by_username(self, username):
        """
        Find a user by their username.

        Args:
            username (str): The username to search for.
        
        Returns:
            User document if found, otherwise None.
        """
        return self.collection.find_one({"username": username})

    def find_user_by_id(self, user_id):
        """
        Find a user by their unique ID.

        Args:
            user_id: The unique ID of the user.
        
        Returns:
            User document if found, otherwise None.
        """
        return self.collection.find_one({"_id": user_id})

    def update_user_status(self, user_id, status):
        """
        Update the status of a user.

        Args:
            user_id: The unique ID of the user.
            status (str): The new status to set (e.g., "active", "pending").
        
        Returns:
            Result of the update operation.
        """
        return self.collection.update_one({"_id": user_id}, {"$set": {"status": status}})

    def delete_user(self, user_id):
        """
        Delete a user by their unique ID.

        Args:
            user_id: The unique ID of the user to delete.
        
        Returns:
            Result of the deletion operation.
        """
        return self.collection.delete_one({"_id": user_id})

    def list_users_by_role(self, role):
        """
        List all users with a specific role.

        Args:
            role (str): The role to filter users by.
        
        Returns:
            List of users with the specified role.
        """
        return list(self.collection.find({"role": role}))

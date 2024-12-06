from pymongo import MongoClient

# Initialize the database connection
client = MongoClient("localhost", 27017)  # Adjust host and port as needed
db = client["hq_database"]  # Replace with your database name

# Export the db instance
__all__ = ["db"]
# Helper functions for input validation

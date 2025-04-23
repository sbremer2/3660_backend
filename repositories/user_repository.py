import json
import os
from models.user_model import User

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
USER_DB_PATH = os.path.join(BASE_DIR, "db", "users.json")

class UserRepository:
    @staticmethod
    def get_user_by_username(username: str) -> User:
        print("DEBUG: USER_DB_PATH =", USER_DB_PATH)
        print("DEBUG: exists?    ", os.path.isfile(USER_DB_PATH))
        try: 
            with open(USER_DB_PATH, "r") as file:
                data = json.load(file)
                for entry in data.get("users", []):
                    if entry.get("username") == username:
                        return User(username=entry["username"], password_hash=entry["password_hash"])
        except FileNotFoundError:
            raise Exception("User file not found")
        
        return None
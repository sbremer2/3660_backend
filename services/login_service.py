import jwt
import hashlib
from datetime import datetime, timezone, timedelta

from repositories.user_repository import UserRepository
from db.db import DatabaseFactory
from config import settings

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
EXP_MINUTES = 5

class LoginService:
    @staticmethod
    def get_login_token(username: str, password: str) -> str:
        # Use database connection
        user_repo = UserRepository(DatabaseFactory())
        user = user_repo.get_user_by_username(username)
        if not user:
            raise Exception("User not found")

        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        if user.password_hash != hashed_password:
            raise Exception("Invalid password")

        now = datetime.now(timezone.utc)
        payload = {
            "sub": user.username,
            "iat": now,
            "exp": now + timedelta(minutes=EXP_MINUTES),
        }

        token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
        return token

    @staticmethod
    def verify_token(token: str) -> dict:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            return payload
        except jwt.ExpiredSignatureError:
            raise Exception("Token has expired")
        except jwt.PyJWTError as e:
            raise Exception(f"Token is invalid: {str(e)}")

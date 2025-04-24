from fastapi import APIRouter
from pydantic import BaseModel
import psycopg2

router = APIRouter()

def get_db_connection():
    return psycopg2.connect(
        host="your-rds-endpoint",
        database="your-db-name",
        user="your-db-user",
        password="your-db-password"
    )

@router.get("/users")
def get_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, username FROM users;")
    users = cur.fetchall()
    cur.close()
    conn.close()
    return [{"id": u[0], "username": u[1]} for u in users]

class NewUser(BaseModel):
    username: str
    password: str

@router.post("/users")
def add_user(user: NewUser):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO users (username, password) VALUES (%s, %s);",
        (user.username, user.password)
    )
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "User added"}

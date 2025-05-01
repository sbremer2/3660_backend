from sqlalchemy import Column, Integer, String
from models.my_base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)

    def __repr__(self):
        return f"User(username={self.username!r})"
    
if __name__ == "__main__":
    print(Base.metadata.tables)
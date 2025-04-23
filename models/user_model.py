class User:
    def __init__(self, username: str, password_hash: str):
        self.username = username
        self.password_hash = password_hash

    def __repr__(self):
        return f"User(username={self.username!r})"
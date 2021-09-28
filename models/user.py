from . import Base, db
from werkzeug.security import generate_password_hash, check_password_hash


class User(Base):
    __tablename__ = "users"
    email = db.Column(db.String(64), index=True, default=None)
    password_hash = db.Column(db.String(128), nullable=False)

    def __init__(self, email=None, password=None):
        self.email = email
        if password:
            self.password_hash = self.hash_password(password)
        super().__init__()

    @staticmethod
    def hash_password(password):
        return generate_password_hash(password)

    def get(self):
        return {
            "id": self.id,
            "email": self.email
        }

    def verify_password(self, new_password):
        return check_password_hash(self.password_hash, new_password)


class Task(Base):
    name = db.Column(db.String(64))

    def __init__(self, name=None):
        self.name = name
        super().__init__()

    def get(self):
        return {
            "id": self.id,
            "name": self.name
        }

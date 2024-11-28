from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    """
    User model representing application users.
    ---
    Fields:
    - userID: Primary key, auto-incremented.
    - username: Unique username of the user.
    - email: Unique email address.
    - password_hash: Hashed password for authentication.
    - preferences: Optional preferences stored as a serialized list.

    Methods:
    - set_password: Hashes the password securely.
    - check_password: Verifies provided password against the stored hash.
    - to_dict: Converts user instance to a dictionary for JSON responses.
    """
    __tablename__ = 'user'

    userID = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    preferences = db.Column(db.PickleType, nullable=True)

    def __init__(self, username, email, password, preferences=None):
        self.username = username
        self.email = email
        self.set_password(password)
        self.preferences = preferences or []

    def set_password(self, password):
        """Hashes and stores the password securely."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Verifies the provided password."""
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        """Converts user instance to a dictionary for JSON responses."""
        return {
            "userID": self.userID,
            "username": self.username,
            "email": self.email,
            "preferences": self.preferences,
        }

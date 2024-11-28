from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Session(db.Model):
    """
    Represents a user session.
    ---
    Fields:
    - sessionID: Primary key, auto-incremented.
    - userID: Foreign key linking to the User model.
    - time: Timestamp when the session started.
    - status: Status of the session (e.g., 'active', 'inactive').

    Methods:
    - to_dict: Converts the session instance to a dictionary.
    """
    __tablename__ = 'session'

    sessionID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userID = db.Column(db.Integer, db.ForeignKey('user.userID'), nullable=False)
    time = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(50), nullable=False)

    # Relationship with User
    user = db.relationship('User', backref='sessions', lazy=True)

    def __init__(self, userID, status, time=None):
        self.userID = userID
        self.status = status
        self.time = time or datetime.utcnow()

    def to_dict(self):
        """
        Converts the session instance to a dictionary for JSON responses.
        """
        return {
            "sessionID": self.sessionID,
            "userID": self.userID,
            "time": self.time.strftime("%Y-%m-%d %H:%M:%S"),
            "status": self.status,
        }

    def __repr__(self):
        """
        String representation for debugging.
        """
        return f"<Session(sessionID={self.sessionID}, userID={self.userID}, status={self.status})>"

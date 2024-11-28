# __init__.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .trip import Trip
from .recommendation import Recommendation
from .feedback import Feedback
from .session import Session

__all__ = ['User', 'Trip', 'Recommendation', 'Feedback', 'Session']

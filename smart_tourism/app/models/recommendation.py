from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Recommendation(db.Model):
    """
    Represents a recommendation for a trip.
    ---
    Fields:
    - recommendationID: Primary key, auto-incremented.
    - userID: Foreign key linking to the User model.
    - tripID: Foreign key linking to the Trip model.
    - rating: Optional rating for the recommendation.

    Methods:
    - update_rating: Updates the rating for the recommendation.
    - to_dict: Converts the recommendation instance to a dictionary.
    """
    __tablename__ = 'recommendation'

    recommendationID = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, db.ForeignKey('user.userID'), nullable=False)
    tripID = db.Column(db.Integer, db.ForeignKey('trip.tripID'), nullable=False)
    rating = db.Column(db.Float, nullable=True)

    # Relationships
    user = db.relationship('User', backref='recommendations')
    trip = db.relationship('Trip', backref='recommendations')

    def __init__(self, userID, tripID, rating=None):
        self.userID = userID
        self.tripID = tripID
        self.rating = rating

    def update_rating(self, new_rating):
        """
        Updates the rating for the recommendation.
        """
        self.rating = new_rating
        db.session.commit()

    def to_dict(self):
        """
        Converts the recommendation instance to a dictionary for JSON responses.
        """
        return {
            "recommendationID": self.recommendationID,
            "userID": self.userID,
            "tripID": self.tripID,
            "rating": self.rating,
        }

    def __repr__(self):
        """
        String representation for debugging.
        """
        return f"<Recommendation User {self.userID} -> Trip {self.tripID}, Rating: {self.rating}>"

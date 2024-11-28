from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Feedback(db.Model):
    """
    Represents feedback for a trip.
    ---
    Fields:
    - feedbackID: Primary key, auto-incremented.
    - userID: Foreign key linking to the User model.
    - tripID: Foreign key linking to the Trip model.
    - comment: Optional feedback comment.
    - rating: Rating for the trip.

    Methods:
    - update_comment: Updates the feedback comment.
    - update_rating: Updates the rating for the feedback.
    - to_dict: Converts the feedback instance to a dictionary.
    """
    __tablename__ = 'feedback'

    feedbackID = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, db.ForeignKey('user.userID'), nullable=False)
    tripID = db.Column(db.Integer, db.ForeignKey('trip.tripID'), nullable=False)
    comment = db.Column(db.String(500), nullable=True)
    rating = db.Column(db.Float, nullable=False)

    # Relationships
    user = db.relationship('User', backref='feedbacks')
    trip = db.relationship('Trip', backref='feedbacks')

    def __init__(self, userID, tripID, comment, rating):
        self.userID = userID
        self.tripID = tripID
        self.comment = comment
        self.rating = rating

    def update_comment(self, new_comment):
        """
        Updates the feedback comment.
        """
        self.comment = new_comment
        db.session.commit()

    def update_rating(self, new_rating):
        """
        Updates the rating for the feedback.
        """
        self.rating = new_rating
        db.session.commit()

    def to_dict(self):
        """
        Converts the feedback instance to a dictionary for JSON responses.
        """
        return {
            "feedbackID": self.feedbackID,
            "userID": self.userID,
            "tripID": self.tripID,
            "comment": self.comment,
            "rating": self.rating,
        }

    def __repr__(self):
        """
        String representation for debugging.
        """
        return f"<Feedback User {self.userID} -> Trip {self.tripID}, Rating: {self.rating}>"

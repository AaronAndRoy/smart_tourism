from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Trip(db.Model):
    """
    Represents a travel trip.
    ---
    Fields:
    - tripID: Primary key, auto-incremented.
    - destination: Destination of the trip.
    - description: Optional description of the trip.
    - cost: Cost of the trip.
    - rating: Optional average rating of the trip.

    Methods:
    - add_review: Adds or updates the trip's average rating.
    - update_trip_details: Updates the trip's details.
    - to_dict: Converts the trip instance to a dictionary.
    """
    __tablename__ = 'trip'

    tripID = db.Column(db.Integer, primary_key=True)
    destination = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    cost = db.Column(db.Float, nullable=False)
    rating = db.Column(db.Float, nullable=True)

    def __init__(self, destination, description, cost, rating=None):
        self.destination = destination
        self.description = description
        self.cost = cost
        self.rating = rating

    def add_review(self, new_rating):
        """
        Adds or updates the trip's average rating.
        ---
        If no rating exists, sets the new rating.
        Otherwise, updates the average rating.
        """
        if self.rating is None:
            self.rating = new_rating
        else:
            self.rating = (self.rating + new_rating) / 2
        db.session.commit()

    def update_trip_details(self, destination=None, description=None, cost=None):
        """
        Updates the trip's details.
        ---
        Accepts partial updates for destination, description, and cost.
        """
        if destination:
            self.destination = destination
        if description:
            self.description = description
        if cost:
            self.cost = cost
        db.session.commit()

    def to_dict(self):
        """
        Converts the trip instance to a dictionary for JSON responses.
        """
        return {
            "tripID": self.tripID,
            "destination": self.destination,
            "description": self.description,
            "cost": self.cost,
            "rating": self.rating
        }

    def __repr__(self):
        """
        String representation for debugging.
        """
        return f"<Trip {self.destination} - ${self.cost}>"

# routes/__init__.py
from app.routes.auth import auth_blueprint
from app.routes.feedback import feedback_bp
from app.routes.recommendation import recommendation_bp

def register_routes(app):
    # Register all blueprints to the Flask app.
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(feedback_bp, url_prefix='/feedback')
    app.register_blueprint(recommendation_bp, url_prefix='/recommendations')  # Fix here

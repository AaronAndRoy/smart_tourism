from flask import Flask
from flask_cors import CORS
from app.models import db
from app.routes import register_routes
from app.db import init_mysql

def create_app():

    #Create and configure the Flask application.

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///smart_tourism.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'your-secret-key'

    # Initialize extensions
    db.init_app(app)  # SQLAlchemy
    init_mysql(app)  # MySQL
    CORS(app)

    # Register routes
    register_routes(app)

    return app

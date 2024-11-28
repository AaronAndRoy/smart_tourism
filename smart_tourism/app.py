from flask import Flask, jsonify
from app.db import mysql
from app.routes.auth import auth_blueprint
from app.routes.recommendation import recommendation_bp
from app.routes.feedback import feedback_bp
import os

def create_app():
    """
    Create and configure the Flask app.
    ---
    Flutter Integration:
    The API server is designed to serve requests from a Flutter app.
    """
    app = Flask(__name__)

    # App configuration
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = '1234'
    app.config['MYSQL_DB'] = 'smart_tourism'

    # Initialize MySQL
    mysql.init_app(app)

    # Register blueprints for modularity
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(recommendation_bp, url_prefix='/recommendations')
    app.register_blueprint(feedback_bp, url_prefix='/feedback')

    # Health check route
    @app.route('/health', methods=['GET'])
    def health_check():
        """
        Health check endpoint to verify server status.
        ---
        Flutter Integration:
        Endpoint: /health
        Method: GET
        Returns: {"status": "ok"}
        """
        return jsonify({"status": "ok"}), 200

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

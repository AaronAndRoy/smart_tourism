from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app.db import mysql

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/register', methods=['POST'])
def register():
    """
    Register a new user.
    ---
    Flutter Integration:
    Endpoint: /register
    Method: POST
    Expected Payload:
    {
        "username": "string",
        "email": "string",
        "password": "string"
    }
    """
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({"error": "Missing required fields"}), 400

    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM user WHERE email = %s", (email,))
        account = cursor.fetchone()

        if account:
            return jsonify({"error": "Account already exists"}), 409

        hashed_password = generate_password_hash(password)
        cursor.execute(
            "INSERT INTO user (username, email, password_hash) VALUES (%s, %s, %s)",
            (username, email, hashed_password),
        )
        mysql.connection.commit()
        return jsonify({"message": "Registration successful"}), 201
    except Exception as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 500
    finally:
        cursor.close()

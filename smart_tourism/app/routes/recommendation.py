from flask import Blueprint, request, jsonify
from app.db import mysql

recommendation_bp = Blueprint('recommend', __name__)

@recommendation_bp.route('/recommendations/<int:userID>', methods=['GET'])
def get_recommendations(userID):
    """
    Fetch recommendations for a user.
    ---
    Flutter Integration:
    Endpoint: /recommendations/<userID>
    Method: GET
    Returns:
    [
        {
            "recommendationID": int,
            "userID": int,
            "tripID": int,
            "rating": float
        }
    ]
    """
    try:
        cursor = mysql.connection.cursor()
        cursor.execute(
            "SELECT recommendationID, userID, tripID, rating FROM recommendation WHERE userID = %s",
            (userID,),
        )
        recommendations = cursor.fetchall()
        cursor.close()

        recommendations_list = [
            {
                "recommendationID": r[0],
                "userID": r[1],
                "tripID": r[2],
                "rating": r[3],
            }
            for r in recommendations
        ]
        return jsonify(recommendations_list), 200
    except Exception as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 500


@recommendation_bp.route('/recommendations', methods=['POST'])
def add_recommendation():
    """
    Add a new recommendation for a user.
    ---
    Flutter Integration:
    Endpoint: /recommendations
    Method: POST
    Expected Payload:
    {
        "userID": int,
        "tripID": int,
        "rating": float
    }
    """
    data = request.json
    userID = data.get('userID')
    tripID = data.get('tripID')
    rating = data.get('rating')

    if not userID or not tripID or rating is None:
        return jsonify({"error": "Missing required fields"}), 400

    try:
        cursor = mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO recommendation (userID, tripID, rating) VALUES (%s, %s, %s)",
            (userID, tripID, rating),
        )
        mysql.connection.commit()
        return jsonify({"message": "Recommendation added successfully"}), 201
    except Exception as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 500
    finally:
        cursor.close()

from flask import Blueprint, request, jsonify
from app.db import mysql

feedback_bp = Blueprint('feedback', __name__)

@feedback_bp.route('/feedback', methods=['POST'])
def submit_feedback():
    """
    Submit feedback for a trip.
    ---
    Flutter Integration:
    Endpoint: /feedback
    Method: POST
    Expected Payload:
    {
        "userID": int,
        "tripID": int,
        "comment": "string",
        "rating": float
    }
    """
    data = request.json
    userID = data.get('userID')
    tripID = data.get('tripID')
    comment = data.get('comment', '')  # Optional
    rating = data.get('rating')

    if not userID or not tripID or rating is None:
        return jsonify({"error": "Missing required fields"}), 400

    try:
        cursor = mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO feedback (userID, tripID, comment, rating) VALUES (%s, %s, %s, %s)",
            (userID, tripID, comment, rating),
        )
        mysql.connection.commit()
        return jsonify({"message": "Feedback submitted successfully"}), 201
    except Exception as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 500
    finally:
        cursor.close()


@feedback_bp.route('/feedback/<int:tripID>', methods=['GET'])
def get_feedback(tripID):
    """
    Get all feedback for a specific trip.
    ---
    Flutter Integration:
    Endpoint: /feedback/<tripID>
    Method: GET
    Returns:
    [
        {
            "feedbackID": int,
            "userID": int,
            "tripID": int,
            "comment": "string",
            "rating": float
        }
    ]
    """
    try:
        cursor = mysql.connection.cursor()
        cursor.execute(
            "SELECT feedbackID, userID, tripID, comment, rating FROM feedback WHERE tripID = %s",
            (tripID,),
        )
        feedbacks = cursor.fetchall()
        cursor.close()

        feedback_list = [
            {
                "feedbackID": f[0],
                "userID": f[1],
                "tripID": f[2],
                "comment": f[3],
                "rating": f[4],
            }
            for f in feedbacks
        ]
        return jsonify(feedback_list), 200
    except Exception as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 500

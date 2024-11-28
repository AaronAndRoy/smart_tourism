from flask_mysqldb import MySQL
from flask import Flask

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'smart_tourism'

mysql = MySQL(app)


# Create tables in the database
def create_tables():
    with app.app_context():  # Create an application context
        cursor = mysql.connection.cursor()

        # Create Users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                userID INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                email VARCHAR(100) NOT NULL UNIQUE,
                password_hash VARCHAR(255) NOT NULL,
                role VARCHAR(50) DEFAULT 'user',
                profile_image VARCHAR(255),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
            )
        ''')

        # Create Trips table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS trips (
                tripID INT AUTO_INCREMENT PRIMARY KEY,
                userID INT NOT NULL,
                destination VARCHAR(255) NOT NULL,
                image_url VARCHAR(255),
                start_date DATE NOT NULL,
                end_date DATE NOT NULL,
                budget FLOAT NOT NULL,
                description TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                FOREIGN KEY (userID) REFERENCES users(userID)
            )
        ''')

        # Create Sessions table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sessions (
                sessionID INT AUTO_INCREMENT PRIMARY KEY,
                userID INT NOT NULL,
                session_token VARCHAR(255) NOT NULL,
                expires_at TIMESTAMP NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                FOREIGN KEY (userID) REFERENCES users(userID)
            )
        ''')

        # Create Recommendations table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS recommendations (
                recommendationID INT AUTO_INCREMENT PRIMARY KEY,
                tripID INT NOT NULL,
                recommendation_text TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                FOREIGN KEY (tripID) REFERENCES trips(tripID)
            )
        ''')

        # Create Feedback table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS feedback (
                feedbackID INT AUTO_INCREMENT PRIMARY KEY,
                userID INT NOT NULL,
                tripID INT NOT NULL,
                feedback_text TEXT NOT NULL,
                rating FLOAT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                FOREIGN KEY (userID) REFERENCES users(userID),
                FOREIGN KEY (tripID) REFERENCES trips(tripID)
            )
        ''')

        # Commit changes and close the cursor
        mysql.connection.commit()
        cursor.close()


if __name__ == '__main__':
    create_tables()
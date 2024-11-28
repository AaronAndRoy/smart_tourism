# db.py
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy

# MySQL Instance
mysql = MySQL()

# SQLAlchemy Instance
db = SQLAlchemy()

def init_mysql(app):
    """
    Initialize MySQL connection with the Flask app.
    """
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = '1234'
    app.config['MYSQL_DB'] = 'smart_tourism'
    mysql.init_app(app)


def setup_database(app):
    """
    Set up database tables (for SQLAlchemy).
    Run this function to create all tables during development.
    """
    with app.app_context():
        db.create_all()

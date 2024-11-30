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
    mysql.init_app(app)

# config.py

# Flask Configuration
SECRET_KEY = 'your-secret-key'

# MySQL Database Configuration
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '1234'
MYSQL_DB = 'smart_tourism'

# SQLAlchemy Configuration
SQLALCHEMY_DATABASE_URI = f'mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = False

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # Secret key for session management and CSRF protection
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')
    
    # Flask application settings
    FLASK_APP = os.getenv('FLASK_APP', 'run.py')
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')

    # Instance path and database URI
    FLASK_INSTANCE_PATH = os.getenv('FLASK_INSTANCE_PATH', os.path.join(os.getcwd(), 'instance'))
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(FLASK_INSTANCE_PATH, 'intelvibez.db')}"
    
    # Additional security configurations
    SESSION_COOKIE_SECURE = os.getenv('SESSION_COOKIE_SECURE', 'True')  # Ensure cookies are secure
    CSRF_ENABLED = True  # Enable CSRF protection if using Flask-WTF

    # SQLAlchemy configurations
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Optional logging configuration
    LOGGING_LEVEL = os.getenv('LOGGING_LEVEL', 'DEBUG')  # Set logging level for debugging
import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(os.getenv('FLASK_INSTANCE_PATH', ''), 'intelvibez.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
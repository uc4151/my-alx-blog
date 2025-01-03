import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize extensions globally
db = SQLAlchemy()
login_manager = LoginManager()

# Set the login view for LoginManager
login_manager.login_view = 'routes.login'

def create_app():
    from .models import User, Post, Comment
    # Create the Flask application
    app = Flask(
        __name__, 
        instance_relative_config=True, 
        template_folder=os.path.join(os.path.dirname(__file__), 'templates')
    )

    # Load configuration from config.py
    app.config.from_object('config.Config')

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Register blueprints
    from .routes import routes
    app.register_blueprint(routes)

    with app.app_context():
        db.create_all()  # Create database tables

    return app
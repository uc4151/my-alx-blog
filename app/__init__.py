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
    # Create the Flask application
    app = Flask(__name__, instance_relative_config=True)

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        # Log if the instance folder already exists or cannot be created
        print(f"Instance folder '{app.instance_path}' already exists or cannot be created.")

    # Load configuration from the Config class
    app.config.from_object('config.Config')

    # Initialize extensions with the Flask app
    db.init_app(app)
    login_manager.init_app(app)

    # Import and register the Blueprint
    from .routes import routes
    app.register_blueprint(routes)

    # Create database tables
    with app.app_context():
        from . import models  # Import models
        db.create_all()  # Create database tables

    # Confirm the app has been created successfully
    print("Flask app created successfully.")
    return app
from app.models import db, User, Post, Comment
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

from app import create_app, db
from app.models import User
from flask_migrate import Migrate

app = create_app()  # Create the app instance using create_app()
migrate = Migrate(app, db)  # Initialize Flask-Migrate with the app and db

@app.login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  # Load user by ID for Flask-Login

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Comment': Comment}

if __name__ == '__main__':
    app.run(debug=True)  # Run the app in debug mode
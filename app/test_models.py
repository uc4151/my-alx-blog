import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import create_app, db
from app.models import Post, Comment

app = create_app()
with app.app_context():
    db.create_all()  # Create tables based on the models
    print("Tables created successfully.")

# Inspect SQLAlchemy metadata for tables
print(db.metadata.tables.keys())  # Lists tables defined by SQLAlchemy models
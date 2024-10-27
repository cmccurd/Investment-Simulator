# This file is where we set up the core of the Flask app.
# By defining the app here, we make it easy to keep everything 
# modular and organized. This function will be the central place 
# to configure Flask settings, initialize the database, and 
# register routes (when we add those next).

from flask import Flask  # Import Flask to create the app
from flask_sqlalchemy import SQLAlchemy # SQLAlchemy for database handling
from dotenv import load_dotenv # To load environment variables
import os  # For interacting with the OS to fetch environment variables

load_dotenv() # Load env variables from .env

db = SQLAlchemy()  # Initialize SQLAlchemy for database interaction

def create_app():
    # Initialize Flask app
    app = Flask(__name__)

     # Load config settings from config.py
    app.config.from_object('config.Config')

    # Initialize extensions like SQAlchemy here
    db.init_app(app)

    # Placeholder to register routes (we’ll add these in routes.py soon)
    # from app.routes import main
    # app.register_blueprint(main)
    
    return app
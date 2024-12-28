from flask import Flask

# Create the Flask app instance
app = Flask(__name__)

# Import routes to register them with the app
from app import routes

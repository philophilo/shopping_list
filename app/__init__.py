from flask import Flask

# Initialize application
app = Flask(__name__, instance_relative_config=True)

# Load views
from app import views

# Linking the configuration file
app.config.from_object('config.BaseConfig')

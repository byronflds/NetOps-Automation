from flask import Flask
from app.extensions import db
import logging
from logging.handlers import RotatingFileHandler
import os
from routes.ports import ports

def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)
    app.config.from_object("config.settings.Config")
    setup_logging(app)

    db.init_app(app)

    from .routes.main import main
    app.register_blueprint(main)
    app.register_blueprint(ports)

    return app 

def setup_logging(app):
    """Set up logging for the Flask application."""
    if not os.path.exists('logs'):
        os.mkdir('logs')
    
    file_handler = RotatingFileHandler('logs/app.log', maxBytes=10240, backupCount=3)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Application startup')
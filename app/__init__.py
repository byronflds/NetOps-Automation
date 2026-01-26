from flask import Flask, render_template
from app.extensions import db
import logging
from logging.handlers import RotatingFileHandler
import os
from .routes.ports import ports
from .routes.billing import billing
from app.extensions import login_manager
from .routes.auth import auth

def register_error_handlers(app):

    @app.errorhandler(403)
    def forbidden(e):
        return render_template("errors/403.html"), 403

    @app.errorhandler(404)
    def not_found(e):
        return render_template("errors/404.html"), 404

def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)
    app.config.from_object("config.settings.Config")
    setup_logging(app)

    db.init_app(app)
    login_manager.init_app(app)

    from .routes.main import main
    app.register_blueprint(main)
    app.register_blueprint(ports)
    app.register_blueprint(billing)
    app.register_blueprint(auth)
    register_error_handlers(app)
    
    from app.models.user import User
    @login_manager.user_loader
    def load_user(user_id):
      return User.query.get(int(user_id))

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
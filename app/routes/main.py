from flask import Blueprint, render_template, current_app
from flask_login import logout_user, login_required

main = Blueprint("main", __name__)

@main.route("/")
@login_required
def index():
    current_app.logger.info("Index page accessed")
    return render_template("index.html")
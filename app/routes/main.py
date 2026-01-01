from flask import Blueprint, render_template, current_app

main = Blueprint("main", __name__)

@main.route("/")
def index():
    current_app.logger.info("Index page accessed")
    return render_template("index.html")
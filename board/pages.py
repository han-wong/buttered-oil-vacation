from flask import Blueprint, render_template

bp = Blueprint("pages", __name__, template_folder='templates')

@bp.route("/")
def home():
    return render_template("pages/home.html")

@bp.route("/about")
def about():
    return render_template("pages/about.html")
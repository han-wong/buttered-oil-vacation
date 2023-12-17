from flask import render_template
from flask_hangman.main import bp

@bp.route('/')
def index():
    return render_template('index.html')
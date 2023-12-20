from flask import render_template
from flask_hangman.main import bp
from flask_hangman import model
from flask import request


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/result", methods=["GET", "POST"])
def result():
    if request.method == "POST" and len(dict(request.form)) > 0:
        userdata = dict(request.form)
        print(userdata)
        book = userdata["book"]
        character = model.get_character(book)
        gif_url = model.get_gif(character)
        return render_template("pages/result.html", character=character, gif_url=gif_url)
    else:
        return "Sorry, there was an error."

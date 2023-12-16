from flask import Flask

from board import pages

def create_app():
    app = Flask(__name__)
    app.config["EXPLAIN_TEMPLATE_LOADING"] = True
    app.register_blueprint(pages.bp)
    print(f"{pages.bp = }")
    return app

if __name__ == "__main__":
    create_app().run() 
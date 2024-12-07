from flask import Flask
from .app import main_app
from .greet import greet_form as gf


def create_app():
    app = Flask(__name__)
    app.secret_key = '1234'

    app.register_blueprint(main_app)
    app.register_blueprint(gf.greet_bp)

    return app

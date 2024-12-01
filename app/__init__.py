from flask import Flask
from .app import main_app


def create_app():
    app = Flask(__name__)
    app.secret_key = '1234'

    app.register_blueprint(main_app)

    return app

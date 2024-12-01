from flask import Flask, render_template, request, flash, Blueprint

main_app = Blueprint('main_app', __name__)


@main_app.route("/")
def index():
    flash("what's your name?")
    return render_template("index.html")


@main_app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hello there, " + str(request.form['name_input']))
    return render_template("index.html")

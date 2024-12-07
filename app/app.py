from flask import Flask, render_template, request, flash, Blueprint

main_app = Blueprint('main_app', __name__)


@main_app.route("/")
def index():
    return render_template("index.html")


@main_app.route("/page1")
def page1():
    return render_template("page1.html")

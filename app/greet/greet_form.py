from flask import Blueprint, render_template, request, flash
from wtforms import Form, StringField, validators


greet_bp = Blueprint('greet', __name__)


class GreetForm(Form):
    user_name = StringField('Name', [validators.Length(min=4, max=25)])
    nick_name = StringField('Nickname', [validators.Length(min=4, max=25)])


@greet_bp.route("/greet", methods=['GET', "POST"])
def greet():
    form = GreetForm(request.form)
    if request.method == 'POST' and form.validate():
        flash("Hello there, " + form.user_name.data +
              ' AKA ' + form.nick_name.data)
    else:
        flash("Write your name")

    return render_template("greet.html", form=form)

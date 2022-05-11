from flask import Blueprint, render_template

auth = Blueprint("auth", __name__)

@auth.route("/sign-up")
def sign_up():
    return render_template("sign_up.html")

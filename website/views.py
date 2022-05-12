from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint("views", __name__)

@views.route("/")
def home():
    return render_template("home.html", user=current_user)

@views.route("/user-home")
@login_required
def user_home():
    return render_template("user_home.html", user=current_user)


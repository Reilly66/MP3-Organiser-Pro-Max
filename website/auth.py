from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from .import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint("auth", __name__)

@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if User.query.filter_by(username=username).first():
            flash("Username is already taken.", "failure")
        elif len(username) < 4:
            flash("Username must be at least 4 characters long.", category="failure")
        elif len(password1) < 8:
            flash("Password must be at least 8 characters long.", category="failure")
        elif not any(char.isdigit() for char in password1):
            flash("Password must contain at least one digit.", category="failure")
        elif password1 != password2:
            flash("Passwords must match.", category="failure")
        else:
            new_user = User(username=username, password=generate_password_hash(password1, method="sha256"))
            db.session.add(new_user)
            db.session.commit()
            flash("Account created.", category="success")
            login_user(new_user, remember=True)
            return redirect(url_for("views.user_home"))

    return render_template("sign_up.html", user=current_user)

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in successfully.", category="success")
                login_user(user, remember=True)
                return redirect(url_for("views.user_home"))
            else:
                flash("Incorrect password.", category="failure")
        else:
            flash("Username does not exist.", category="failure")

    return render_template("login.html", user=current_user)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("views.home"))

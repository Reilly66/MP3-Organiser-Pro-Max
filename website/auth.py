from flask import Blueprint, render_template, request, flash

auth = Blueprint("auth", __name__)

@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if len(username) < 4:
            flash("Username must be at least 4 characters long.", category="failure")
        elif len(password1) < 8:
            flash("Password must be at least 8 characters long.", category="failure")
        elif not any(char.isdigit() for char in password1):
            flash("Password must contain at least one digit.", category="failure")
        elif password1 != password2:
            flash("Passwords must match.", category="failure")
        else:
            flash("Account created.", category="success")
            # add user to the database

    return render_template("sign_up.html")

@auth.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")

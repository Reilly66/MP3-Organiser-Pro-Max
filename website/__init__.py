from this import d
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "69420"
    return app

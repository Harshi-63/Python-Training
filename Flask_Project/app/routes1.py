from flask import Blueprint

auth = Blueprint("auth", __name__)


@auth.route("/auth")
def home():
    return "Hello this auth folder"
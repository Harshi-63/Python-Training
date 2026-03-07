from flask import Blueprint, request, jsonify
from .models import Users
from . import db

main = Blueprint("main", __name__)
auth = Blueprint("auth", __name__)


@main.route("/")
def home():
    return "Hello world"


@main.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    # 🛑 if no JSON received
    if not data:
        return jsonify({"message": "No JSON data received"}), 400

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    # 🛑 check empty fields
    if not username or not email or not password:
        return jsonify({"message": "All fields are required"}), 400

    # 🛑 check duplicate email
    if Users.query.filter_by(email=email).first():
        return jsonify({"message": "Email already exists"}), 400

    # ✅ create user
    new_user = Users(
        name=username,
        email=email,
        password=password
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201


@main.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data:
        return jsonify({"message": "No JSON data received"}), 400

    user_email = data.get("email")
    user_password = data.get("password")

    if not user_email or not user_password:
        return jsonify({"message": "Email and password required"}), 400

    # find user
    user = Users.query.filter_by(email=user_email).first()

    # check password
    if user and user.password == user_password:
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid email or password"}), 401

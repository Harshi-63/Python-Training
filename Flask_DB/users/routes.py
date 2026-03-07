from flask import Blueprint, jsonify

user = Blueprint('user', __name__)


# /user/profile
@user.route('/profile')
def profile():
    return jsonify({
        "username": "Harshita",
        "role": "user"
    })


# /user/settings
@user.route('/settings')
def settings():
    return jsonify({
        "theme": "dark",
        "notifications": True
    })

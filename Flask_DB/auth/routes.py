from flask import Blueprint, request, jsonify

auth = Blueprint('auth', __name__, url_prefix='/auth')


# /auth/register
@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    return jsonify({
        "message": "User registered successfully",
        "user": data
    })


# /auth/login
@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    return jsonify({
        "message": "Login successful",
        "user": data
    })


# /auth/logout
@auth.route('/logout')
def logout():
    return jsonify({"message": "Logged out successfully"})

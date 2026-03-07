from flask import Flask
from admin.routes import admin
from api.routes import api
from users.routes import user
from auth.routes import auth


def create_app():
    app = Flask(__name__)

    app.register_blueprint(admin, url_prefix='/admin')
    app.register_blueprint(api, url_prefix='/api')
    app.register_blueprint(user, url_prefix='/user')
    app.register_blueprint(auth, url_prefix='/auth')

    @app.route('/')
    def home():
        return 'Welcome to the Flask App'
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

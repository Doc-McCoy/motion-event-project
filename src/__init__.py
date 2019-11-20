from flask import Flask

def create_app():

    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    from server.api import api as api_blueprint
    app.register_blueprint(api_blueprint)

    return app

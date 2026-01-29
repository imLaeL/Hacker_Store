from flask import Flask
from .database import engine, Base
from .routes import routes

def create_app():
    app = Flask(__name__)
    app.config["JSON_SORT_KEYS"] = False

    Base.metadata.create_all(engine)

    app.register_blueprint(routes)

    return app

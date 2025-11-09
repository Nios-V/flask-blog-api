from flask import Flask
from flask_cors import CORS
from .config import Config
from .extensions import migrate, jwt
from .models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    CORS(app) # TODO: Limit CORS origins

    with app.app_context():
        db.create_all()

    return app
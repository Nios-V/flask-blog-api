from flask import Flask
from flask_cors import CORS
from .config import Config
from .extensions import db, migrate, jwt
from sqlalchemy import text
from .blueprints import register_blueprints
from flasgger import Swagger

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    CORS(app) # TODO: Limit CORS origins

    Swagger(app)

    register_blueprints(app)

    return app
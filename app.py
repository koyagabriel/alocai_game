from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

from config import config

db: SQLAlchemy = SQLAlchemy()
migrate: Migrate = Migrate()


def create_app(configuration_name: str) -> Flask:
    app: Flask = Flask(__name__)
    app.config.from_object(config[configuration_name])
    db.init_app(app)
    migrate.init_app(app, db)
    Swagger(app)
    
    from src.v1 import v1
    app.register_blueprint(v1)
    return app


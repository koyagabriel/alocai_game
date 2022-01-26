from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import config

db = SQLAlchemy()
migrate = Migrate()


def create_app(configuration_name):
    app = Flask(__name__)
    app.config.from_object(config[configuration_name])
    db.init_app(app)
    migrate.init_app(app, db)
    return app


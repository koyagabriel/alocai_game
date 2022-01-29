from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flasgger import Swagger
from typing import Dict, Any

from config import config

db: SQLAlchemy = SQLAlchemy()
migrate: Migrate = Migrate()
ma: Marshmallow = Marshmallow()
template: Dict[str, Any] =  {
    "swagger": "2.0",
    "info": {
        "title": "Alocai Games",
        "description": "API for my data",
        "contact": {
        "responsibleOrganization": "Alocai",
        "responsibleDeveloper": "Koya Adegboyega",
        "email": "koyexes@gmail.com",
        "url": "www.me.com",
        },
        "termsOfService": "http://me.com/terms",
        "version": "0.0.1"
    },
    "host": "localhost:5000",  # overrides localhost:5000
    # "basePath": "/api",  # base bash for blueprint registration
    "schemes": [
        "http",
        "https"
    ]
}

def create_app(configuration_name: str) -> Flask:
    app: Flask = Flask(__name__)
    app.config.from_object(config[configuration_name])
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    Swagger(app, template=template)
    from src.v1 import v1
    app.register_blueprint(v1)
    return app


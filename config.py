import os
from dotenv import load_dotenv
from typing import Dict, Any

dotenv_path: str = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)


class Config:
    ENV: str = os.environ.get('FLASK_ENV')
    POSTGRES_PASSWORD: str = os.environ.get('POSTGRES_PASSWORD')
    POSTGRES_DB: str = os.environ.get('POSTGRES_DB')
    POSTGRES_HOST: str = os.environ.get('POSTGRES_HOST')
    POSTGRES_USER: str = os.environ.get('POSTGRES_USER')
    POSTGRES_PORT: str = os.environ.get('POSTGRES_PORT')
    SWAGGER: Dict[str, Any] = {
        'title': 'Alocai Games',
        'uiversion': 3,
        'specs': [
            {
                'endpoint': '/',
                'route': '/apispec_1.json',
                'rule_filter': lambda rule: True,
                'model_filter': lambda tag: True,
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/docs/",
    }
    SQLALCHEMY_DATABASE_URI: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
class DevelopmentConfig(Config):
   pass
   
class TestingConfig(Config):
    pass
    
class ProductionConfig(Config):
    pass
    
    
config: Dict[str, Config] = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig
}
import os
from dotenv import load_dotenv
from typing import Dict, Any

dotenv_path: str = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)


class Config:
    ENV: str = os.environ.get('ENV')
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
    SQLALCHEMY_DATABASE_URI: str = os.environ.get("SQLALCHEMY_DATABASE_URI")
class DevelopmentConfig(Config):
   pass
   
class TestingConfig(Config):
    ENV: str = "testing"
    TESTING: bool = True
    
class ProductionConfig(Config):
    pass
    
    
config: Dict[str, Config] = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig
}
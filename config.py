from ast import Pass
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)


class Config:
    ENV = os.environ.get('ENV')
  
  
class DevelopmentConfig(Config):
    pass
   
   
class TestingConfig(Config):
    ENV = "testing"
    TESTING = True
    

class ProductionConfig(Config):
    pass
    
    
config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig
}
from ast import Pass
import os
from dotenv import load_dotenv

dotenv_path: str = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)


class Config:
    ENV: str = os.environ.get('ENV')
  
  
class DevelopmentConfig(Config):
    pass
   
   
class TestingConfig(Config):
    ENV: str = "testing"
    TESTING: bool = True
    

class ProductionConfig(Config):
    pass
    
    
config: dict[str, Config] = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig
}
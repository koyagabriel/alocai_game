import os
from dotenv import load_dotenv
from flask import Flask
from app import create_app

dotenv_path: str  = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)

app: Flask = create_app(os.environ.get("FLASK_ENV"))


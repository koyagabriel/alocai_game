from flask import Blueprint

v1: Blueprint = Blueprint('v1', __name__,  url_prefix='/api/v1')

from . import models, urls, schemas

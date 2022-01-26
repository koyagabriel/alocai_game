from flask import Blueprint

v1: Blueprint = Blueprint('v1', __name__,  url_prefix='/v1')

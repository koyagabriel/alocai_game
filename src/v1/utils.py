from flask import jsonify, Response
from typing import Dict, Any, Optional
from sqlalchemy.sql import text
from app import db
from src.v1.exceptions import ValidationException

def test_database_connection() -> bool:
    try:
        db.session.query(text('1')).from_statement(text('SELECT 1')).all()
        return True
    except:
        return False


def respond_to_json(data: Optional[Dict[Any, Any]] = None, status_code: int = 200) -> Response:
    return jsonify(data), status_code

def get_json(request) -> Dict[str, Any]:
    """
    this function tries to extract data from the json request and raises
    an error if the data is not json serializable
    """
    try:
       return request.json
    except Exception:
        raise ValidationException("The inputted data is not in json format", propagate=True)
from flask import jsonify, request, Response
from flasgger import swag_from, validate
from typing import Dict, Any
from app import db
from src.v1.decorators import catch_exceptions
from src.v1.utils import test_database_connection, respond_to_json, get_json
from src.v1.exceptions import SwaggerException
from src.v1.models import Game
from src.v1.schemas import GameSchema


def index():
    return jsonify({"name": "Alocia games"})

@swag_from("docs/database_status.yml")
@catch_exceptions("Failed to get database status")
def get_database_status() -> Response:
    healthy: bool = test_database_connection()
    method: str = request.method
    health_status: str = "healthy" if healthy else "unhealthy"
    data: Dict[str, str] = {"database": health_status}
    
    if (method == "GET"):
        status_code: int = 200 if healthy else 503
        return respond_to_json(data=data, status_code=status_code)
    
    status_code = 204 if healthy else 503
    return respond_to_json(status_code=status_code)


@swag_from("docs/post_games.yml")
@catch_exceptions("Failed to post a game")
def post_games() -> Response:
    validate(
        request.json, "Game", 
        "docs/post_games.yml", 
        validation_error_handler=SwaggerException.handler
    )
    data: Dict[str, Any] = GameSchema().load(get_json(request))
    game: Dict[str, Any] = GameSchema().dump(Game.create(data))
    return respond_to_json(data=game, status_code=201)
    
from marshmallow import fields, validates, ValidationError
from app import ma
from src.v1.models import Game

class GameSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Game
    name = fields.String(required=True)
    
    @validates("name")
    def validate_name(self, value):
        game: Game = Game.filter_by_name(value)
        if game: raise ValidationError(f"The name '{value}' already exists. Please choose another name.")

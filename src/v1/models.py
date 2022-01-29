from datetime import datetime
from pydoc import classname
from app import db
from typing import List


class BaseMixin(object):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow, default=datetime.utcnow())
    
    def save(self):
        db.session.flush()
        db.session.add(self)
        db.session.commit()


class Game(BaseMixin, db.Model):
    __tablename__ = "games"
    name = db.Column(db.String(128), nullable=False, unique=True)
    price = db.Column(db.DECIMAL, nullable=False)
    space = db.Column(db.BigInteger, nullable=False)
    
    @classmethod
    def create(cls, params):
        game_instance: cls = cls(**params)
        game_instance.save()
        return game_instance
    
    @classmethod
    def filter_by_name(cls, name, many=False):
        query_set = cls.query.filter_by(name=name)
        if many:
            return query_set.all()
        return query_set.first()
    
    @classmethod
    def fetch_best_value_games(cls, pen_drive_space: int):
        query_set = cls.query.filter(cls.space <= pen_drive_space).order_by(cls.space)
        list_of_games: List[cls]  = []
        total_space: int = 0
        remaining_space: int = pen_drive_space
        for game in query_set:
            game_space: int = game.space
            if remaining_space >= game_space:
                list_of_games.append(game)
                total_space += game_space
                remaining_space -= game_space
            else:
                break
        
        return (list_of_games, total_space, remaining_space)

        


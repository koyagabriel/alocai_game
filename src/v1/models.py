
from datetime import datetime
from pydoc import classname
from app import db
from typing import List
import copy


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
    
    
    LIST_OF_GAMES = []
    SPACE_SUM = 0
    
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
        query_set = cls.query.filter(cls.space <= pen_drive_space).order_by(cls.space).all()
        output = []
        result = []
        cls.get_highest_possible_combination(pen_drive_space, 0, query_set, output, result)
        return output
    
    @classmethod
    def get_highest_possible_combination(cls, target, current_sum, start, output, result):
        if current_sum <= target or not start:
            if not output:
                output.append([copy.copy(result), current_sum])
            elif (output[0][1] < current_sum) or (len(output[0][0]) < len(result)):
                output[0] = [copy.copy(result), current_sum]

        for i in range(len(start)):
            temp_sum = current_sum + start[i].space
            if temp_sum <= target:
                result.append(start[i])
                cls.get_highest_possible_combination(target, temp_sum, start[i+1:], output, result)
                result.pop()
            else:
                return



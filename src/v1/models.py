from datetime import datetime
from app import db


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


from datetime import datetime
from app import db


class BaseMixin(object):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow, default=datetime.utcnow())


class Game(BaseMixin, db.Model):
    __tablename__ = "games"
    name = db.Column(db.String(128), nullable=False, unique=True)
    price = db.Column(db.DECIMAL, nullable=False)
    space = db.Column(db.BigInteger, nullable=False)
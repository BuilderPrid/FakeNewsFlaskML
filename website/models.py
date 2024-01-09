from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Result(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(300))
    date = db.Column(db.DateTime(timezone = True),default=func.now())
    result = db.Column(db.Boolean())
    userId = db.Column(db.Integer,db.ForeignKey('user.id'))


class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key = True)
    first_name = db.Column(db.String(100))
    email = db.Column(db.String(150))
    password = db.Column(db.String(200))
    results = db.relationship('Result')
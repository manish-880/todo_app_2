# from flask_sqlalchemy import SQLAlchemy
# from . import db
# from flask_login import UserMixin
# from sqlalchemy.sql import func

# db=SQLAlchemy()

# class Note(db.Model):
#     id = db.Column(db.Integer,primary_key=True)
#     data=db.Column(db.String(10000))
#     date=db.Column(db.DateTime(timezone=True),default=func.now())
#     user_id =db.Column(db.Integer ,db.ForeignKey('user.id'))

# class User(db.Model , UserMixin):
#     id=db.Column(db.Integer,primary_key=True)
#     email=db.Column(db.String,unique=True,nulllable=False)
#     password = db.Column(db.String, nullable=False)
#     role = db.Column(db.Integer, default=1)
#     username = db.Column(db.String, nullable=False)
#     notes=db.relationship('Note')

 

from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime
import pytz


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    date_created = db.Column(db.DateTime, default=lambda: datetime.now(pytz.timezone('Asia/Kolkata')))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    username = db.Column(db.String(150))
    notes = db.relationship('Note')
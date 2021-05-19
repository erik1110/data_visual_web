from flask_sqlalchemy import SQLAlchemy
from app.views import app

db = SQLAlchemy(app)

# 定義 Users 模型
class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    sex = db.Column(db.String(1), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    mail = db.Column(db.String(255), nullable=False)
    birthday = db.Column(db.String(12))
    country = db.Column(db.String(255))
    job = db.Column(db.String(255))
    phone_number = db.Column(db.String(255))
    date = db.Column(db.String(12))
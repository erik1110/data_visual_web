from config import Config, ProductionConfig, DevelopmentConfig, TestingConfig
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask import jsonify
from flask import request
from app.models import Users

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)

@app.route('/')
def index():
    return 'My Flask App!'

@app.route('/create_data', methods=['POST'])
def create_data():
    user_info = Users({
                 "user_id": request.form.get('user_id'),
                 "username": request.form.get('username'),
                 "name": request.form.get('name'),
                 "sex": request.form.get('sex'),
                 "address": request.form.get('address'),
                 "mail": request.form.get('mail'),
                 "birthdate": request.form.get('birthdate'),
                 "country": request.form.get('country'),
                 "job": request.form.get('job'),
                 "phone_number": request.form.get('phone_number'),
                 "date": request.form.get('date'),
                })
    db.session.add(user_info)
    db.session.commit()
    print("寫入資料成功")
    return jsonify(user_info)

    
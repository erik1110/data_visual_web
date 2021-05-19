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
    print("="*50)
    user_info = {
                 "user_id": request.args['user_id'],
                 "username": request.args['username'],
                 "name": request.args['name'],
                 "sex": request.args['sex'],
                 "address": request.args['address'],
                 "mail": request.args['mail'],
                 "birthday": request.args['birthday'],
                 "country": request.args['country'],
                 "job": request.args['job'],
                 "phone_number": request.args['phone_number'],
                 "date": request.args['date']
                }
    print("user_info:", user_info)
    user = Users(**user_info)
    db.session.add(user)
    db.session.commit()
    print("寫入資料成功")
    return jsonify(user_info)

@app.route('/say_hello', methods=['POST'])
def submit():
    name = request.args['username']
    print("name", str(name))
    return "Hello, " + str(name)

    
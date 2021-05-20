from config import Config, ProductionConfig, DevelopmentConfig, TestingConfig
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template
from app.models import Users
import plotly as py
import json

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)

@app.route('/')
def index():
    return 'My Flask App!'

@app.route('/create_data', methods=['POST'])
def create_data():
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
    user = Users(**user_info)
    db.session.add(user)
    db.session.commit()
    print("寫入資料成功")
    return jsonify(user_info)

@app.route('/graph')
def graph():
    users = Users.query.limit(5).all()
    return json.dumps(Users.serialize_list(users), ensure_ascii=False)

@app.route('/say_hello', methods=['POST'])
def submit():
    name = request.args['username']
    print("name", str(name))
    return "Hello, " + str(name)

@app.route('/graph_demo')
def graph_demo():
    # 設置圓餅圖資料
    pie = {
        'values': [100, 50, 30, 20],
        'labels': ['香蕉', '蘋果', '水梨', '草莓'],
        'type': 'pie'
    }

    # 將相關圖表物件以list方式寫入
    graphs = [
        dict(
            data=[
                pie
            ],
            layout=dict(
                width='100%',
                height='100%'
            )
        )
    ]

    # 序列化
    graphJSON = json.dumps(graphs, cls=py.utils.PlotlyJSONEncoder)

    return render_template('pyplot.html', graphJSON=graphJSON)

    
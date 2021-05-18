from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app.views import app

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# 設定你的 app
manager = Manager(app)
# 設定 python manage.py db 來管理 models
manager.add_command('db', MigrateCommand)
# 設定 python manage.py runserver 為啟動 server 指令
manager.add_command('runserver', Server())

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

if __name__ == '__main__':
    manager.run()

    
    
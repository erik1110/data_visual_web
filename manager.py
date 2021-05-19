from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app.models import db
from app.views import app

migrate = Migrate(app, db)

# 設定你的 app
manager = Manager(app)
# 設定 python manage.py db 來管理 models
manager.add_command('db', MigrateCommand)
# 設定 python manage.py runserver 為啟動 server 指令
manager.add_command('runserver', Server())

if __name__ == '__main__':
    manager.run()

    
    
# data_visual_web

## 下載 Postgresql

## 安裝套件
```terminal=
pip install flask==1.1.1 --user
pip install flask_migrate==2.7.0 --user
```
## 使用方法
初始化
```terminal=
python3 manager.py db init
```
migrate
```terminal=
python3 manager.py db migrate
```
upgrade
```terminal=
python3 manager.py db upgrade
```
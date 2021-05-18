from config import Config, ProductionConfig, DevelopmentConfig, TestingConfig
from flask import Flask

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

@app.route('/')
def index():
    return 'My Flask App!'

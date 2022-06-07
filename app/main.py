from flask import Flask, abort, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy()

# REST API を定義
# app.register_blueprint(hello, url_prefix='/api')
users = [
    { "name" : "山田太郎"},
    { "name" : "上田二郎"},
    { "name" : "田中三郎"}
]


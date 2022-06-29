from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from database import init_db
# from sqlalchemy import create_engine

app = Flask(__name__)

# データベース初期化
# def init_db(app):
#   db.init_app(app)

# データベース接続情報
# engine = create_engine("postgresql///?User=matsumoto&Password=assassin&Database=Omailey&Server=127.0.0.1&Port=5432")
class DevConfig:
    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{password}@{host}/{dbname}?charset=utf8'.format(**{
        'user': 'matsumoto',
        'password': 'assassin',
        'host': '127.0.0.1:5432',
        'dbname':'omailey'
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

Config = DevConfig

db = SQLAlchemy()

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, default='')
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)


# REST API を定義
# app.register_blueprint(hello, url_prefix='/api')

@app.route('/')
def index():
    return "Index page"

# query parameter
@app.route('/users', methods=['GET'])
def query_users():
    users = User.query.all()
    print(users[0])
    id = request.args.get("id")
    return id


# def get_db():#データベースのコネクションを取得
#     db = getattr(g, '_database', None)
#     if db is None:
#         db = g._database = sqlite3.connect(dbpath)
#         db.execute('CREATE TABLE IF NOT EXISTS tweets_tbl(id INTEGER PRIMARY KEY AUTOINCREMENT, tweet VARCHAR(140))')
#     return db 
              
# @app.route('/tweet', methods=['GET'])
# def get_tweet():
#     con = get_db() #コネクションを取得
#     con.row_factory = sqlite3.Row #カラム名取得のため
#     cur = con.cursor() #カーソル取得

if __name__ == "__main__":
    app.run() 
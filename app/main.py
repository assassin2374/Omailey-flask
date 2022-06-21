from flask import Flask, abort, Request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()

engine = create_engine("postgresql///?User=postgres&Password=admin&Database=postgres&Server=127.0.0.1&Port=5432")

# REST API を定義
# app.register_blueprint(hello, url_prefix='/api')
users = [
    { "name" : "山田太郎"},
    { "name" : "上田二郎"},
    { "name" : "田中三郎"}
]


@app.route('/')
def index():
    return "Index page"

# query parameter
@app.route('/tasks', methods=['GET'])
def query_tasks():
    users = User.query.all()
    print(users[0].to_dict())
    id = request.args.get("id")
    return id



def get_db():#データベースのコネクションを取得
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(dbpath)
        db.execute('CREATE TABLE IF NOT EXISTS tweets_tbl(id INTEGER PRIMARY KEY AUTOINCREMENT, tweet VARCHAR(140))')
    return db 
              
@app.route('/tweet', methods=['GET'])
def get_tweet():
    con = get_db() #コネクションを取得
    con.row_factory = sqlite3.Row #カラム名取得のため
    cur = con.cursor() #カーソル取得

if __name__ == "__main__":
    app.run() 
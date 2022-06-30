import json
from flask import Flask, request
from application import app
from models import User

# query parameter
# users
@app.route('/users', methods=['GET'])
def query_users():
    users = User.query.all()
    print(users[0].to_dict())
    id = request.args.get("id")
    return users[0].to_dict()

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
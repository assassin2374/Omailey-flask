import json
from flask import request
from application import app
from models.user import User

# query parameter
# users
@app.route('/users', methods=['GET'])
def query_users():
    users = User.query.all()
    print(users[0].to_dict())
    id = request.args.get('id')
    return users[0].to_dict()

@app.route('/users', methods=['POST'])
def create_user():
    result = json.loads(request.data)
    return result

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id = None):
    return 'update' + str(user_id)

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id = None):
    return 'delete' + str(user_id)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
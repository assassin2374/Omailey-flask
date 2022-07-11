


@app.route('/users', methods=['GET'])
def query_users():
    users = User.query.all()
    print(users[0].to_dict())
    id = request.args.get('id')
    return users[0].to_dict()
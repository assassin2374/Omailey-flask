

def query_users():
    users = User.query.all()
    return users[0].to_dict()
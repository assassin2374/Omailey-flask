from flask import request
from application import app
from models.user import User
from IUserService import UserService

class UserController():


  @app.route('/users', methods=['GET'])
  def query_users():
      users = User.query.all()
      print(users[0].to_dict())
      id = request.args.get('id')
      return users[0].to_dict()
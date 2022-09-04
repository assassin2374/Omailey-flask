from flask import request
from application import app
from models.user import User
from .i_user_repository import IUserRepository

class UserRepository(IUserRepository):
    def __init__(self, session):
        self.session = session

    def get_id_user(self, user_id):
        user = self.session.query(User).get(user_id)
        return user

    def create_user(self, user):
        pass

    def update_user(self, user_id, user):
        pass

    def delete_user(self, user_id):
        pass
from abc import ABCMeta, abstractmethod

class IUserRepository(metaclass=ABCMeta):
  @abstractmethod
  def get_id_user(self, user_id):
    pass

  @abstractmethod
  def create_user(self, user):
    pass

  @abstractmethod
  def update_user(self, user_id, user):
    pass

  @abstractmethod
  def delete_user(self, user_id):
    pass
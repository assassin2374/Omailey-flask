from abc import ABC, abstractmethod

class UserRepository(metaclass=ABC):
  @abstractmethod
  def to_dict(self):
    pass
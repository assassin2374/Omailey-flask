from abc import ABC, abstractclassmethod, abstractmethod

class User(metaclass=ABC):
  @abstractmethod
  def __init__(self, id, name, email, password):
    pass
    
  @abstractmethod
  def to_dict(self):
    pass
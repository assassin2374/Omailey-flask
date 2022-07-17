from abc import ABC, abstractmethod

class Model(metaclass=ABC):
  @abstractmethod
  def to_dict(self):
    pass
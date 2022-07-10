from abc import ABC, abstractmethod

class Models(metaclass=ABC):
  @abstractmethod
  def to_dict(self):
    pass
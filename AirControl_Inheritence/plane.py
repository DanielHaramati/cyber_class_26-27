from abc import ABC, abstractmethod


class Plane(ABC):
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y
    @abstractmethod
    def update_position(self):
        pass

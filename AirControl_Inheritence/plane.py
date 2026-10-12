from abc import ABC, abstractmethod


MIN_CELL, MAX_CELL = 0, 9
CRAZY_STEP = 1
class Plane(ABC):
    def __init__(self, pos, name):
        self.__pos = pos
        self.__name = name
    @abstractmethod
    def update_position(self) -> None:
        """Move the plane one step according to its movement pattern.
                Every subclass must implement its own movement logic here.
                """
        pass
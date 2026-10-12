import random
from position import Position


MIN_CELL, MAX_CELL = 0, 9
CRAZY_STEP = 1

class CrazyPlane:


    def __init__(self, position=None, name=None):

        self.__position = position
        self.__name = name

    def update_position(self) -> None:
        self.__position.move_random_in_boundaries(CRAZY_STEP, (MIN_CELL, MAX_CELL), (MIN_CELL, MAX_CELL))


    def goto(self, new_position) -> None:

        new_x = new_position.get_x()
        new_y = new_position.get_y()
        self.__position.goto_position_in_boundaries(new_x, new_y, (MIN_CELL, MAX_CELL), (MIN_CELL, MAX_CELL))

    def get_position(self) :

        return self.__position

    def __str__(self) -> str:
        return f"plane: {self.__name} {self.__position}"

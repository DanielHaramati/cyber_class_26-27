import random


class Position:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def set_x(self, val):
        self.__x = val

    def get_y(self):
        return self.__y

    def set_y(self, val):
        self.__y = val

    def distance(self, other_position) -> float:
        return ((self.__x - other_position.__x) ** 2 + (self.__y - other_position.__y) ** 2) ** 0.5

    def move_random(self, step=1):
        self.__x += random.randint(-step, step)
        self.__y += random.randint(-step, step)

    def move_random_in_boundaries(self, step=1, x_boundaries=None, y_boundaries=None):
        self.move_random(step)
        self.goto_position_in_boundaries(self.__x, self.__y, x_boundaries, y_boundaries)

    def get_position(self):
        return self.__x, self.__y

    def goto_position_in_boundaries(self, new_x, new_y, x_boundaries, y_boundaries):
        if x_boundaries[0] > new_x:
            new_x = x_boundaries[0]
        elif x_boundaries[1] < new_x:
            new_x = x_boundaries[1]
        if y_boundaries[0] > new_y:
            new_y = y_boundaries[0]
        elif y_boundaries[1] < new_y:
            new_y = y_boundaries[1]
        self.__x = new_x
        self.__y = new_y

    def get_possible_moves_in_boundaries(self, step=1, x_boundaries=None, y_boundaries=None):
        moves = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # תנועות אפשריות
        for dx, dy in directions:
            new_x, new_y = self.__x + dx, self.__y + dy
            if x_boundaries[0] <= new_x <= x_boundaries[1] and y_boundaries[0] <= new_y <= y_boundaries[1]:
                moves.append(Position(new_x, new_y))
        return moves

    def __str__(self):
        return f"located at ({self.__x}, {self.__y})"


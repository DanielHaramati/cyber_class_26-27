

import random
import time
from typing import List, Tuple
from crazy_plane import CrazyPlane
from position import Position

MIN_CELL, MAX_CELL = 0, 9   # גבולות המשחק (מערכת קואורדינטות 0 עד 9)
CRAZY_STEP = 1  # מספר תאים שהמטוס יכול לזוז בכל צעד
NUMBER_OF_PLANES = 4  # מספר המטוסים במשחק
ROUNDS = 10


def allocate_planes_on_game_board(number_of_planes: int) -> List["CrazyPlane"]:
    planes = []
    for i in range(1, number_of_planes + 1):
        planes.append(CrazyPlane(Position(random.randint(MIN_CELL, MAX_CELL),
                                          random.randint(MIN_CELL, MAX_CELL)), str(i)))
    return planes


def keep_in_game_boundaries(val: int) -> int:
    if val > MAX_CELL:
        return MAX_CELL
    elif val < MIN_CELL:
        return MIN_CELL
    else:
        return val


def distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> float:

    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


def avoid_collision(planes: List[CrazyPlane]) -> None:
    collision_detected = True
    while collision_detected:
        collision_detected = False
        for i, plane in enumerate(planes):
            # x, y = plane.get_position()
            plane_position = plane.get_position()
            for other_plane in planes[:i] + planes[i + 1:]:
                # other_x, other_y = other_plane.get_position()
                other_plane_position = other_plane.get_position()
                # if distance((x, y), (other_x, other_y)) < 2:
                if plane_position.distance(other_plane_position) < 2:

                    possible_moves = plane_position.get_possible_moves_in_boundaries(CRAZY_STEP,
                                                                                     (MIN_CELL, MAX_CELL),
                                                                                     (MIN_CELL, MAX_CELL))
                    if possible_moves:
                        new_position = random.choice(possible_moves)
                        print(f"turn {plane} to {new_position}")
                        plane.goto(new_position)
                        collision_detected = True


def main() -> None:

    try:
        planes = allocate_planes_on_game_board(NUMBER_OF_PLANES)
        game_round = 1
        while game_round < ROUNDS + 1:
            print("-" * 10, f"round {game_round}", "-" * 10)
            game_round += 1
            for plane in planes:
                plane.update_position()


            avoid_collision(planes)


            print("\n".join(str(plane) for plane in planes))


            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        print("Game ended")


if __name__ == "__main__":
    main()

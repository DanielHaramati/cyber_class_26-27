"""
מודול זה מדמה משחק שבו מטוסים ("Crazy Planes") נעים באופן רנדומלי בלוח דו-ממדי בגבולות מוגדרים.
המודול כולל את האלמנטים הבאים:
1. מחלקה לייצוג מטוס משוגע (CrazyPlane) עם תכונות למיקום ותנועה.
2. פונקציות לניהול גבולות המשחק, מניעת התנגשויות, וחישוב תנועות אפשריות.
3. מנוע משחק שמבצע סבבים של תנועה רנדומלית, הדפסת מצב המשחק, ומניעת התנגשויות.

המטרה היא להדגים את השילוב בין אובייקטים, תנועה רנדומלית, ובדיקות לוגיות בלוח משחק.
"""

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
    """
     פונקציה להקצאת מטוסים על לוח המשחק
    יוצר וממקם מטוסים במספר אקראי של תאים בלוח המשחק.

    :param number_of_planes: מספר המטוסים שיש למקם בלוח.
    :return: רשימה של עצמים מסוג CrazyPlane.
    """
    planes = []
    for i in range(1, number_of_planes + 1):
        planes.append(CrazyPlane(Position(random.randint(MIN_CELL, MAX_CELL),
                                          random.randint(MIN_CELL, MAX_CELL)), str(i)))
    return planes


def keep_in_game_boundaries(val: int) -> int:
    """
    פונקציה לבדיקת גבולות
    מבטיחה שהערך יישאר בגבולות המוגדרים של המשחק.

    :param val: הערך לבדיקה.
    :return: ערך מתוקן אם יצא מהגבולות, אחרת מחזירה את הערך המקורי.
    """
    if val > MAX_CELL:
        return MAX_CELL
    elif val < MIN_CELL:
        return MIN_CELL
    else:
        return val


def distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> float:
    """
    חישוב המרחק בין שני מטוסים
    מחשבת את המרחק האוקלידי בין שני נקודות.

    :param p1: הנקודה הראשונה כזוג קואורדינטות (x1, y1).
    :param p2: הנקודה השנייה כזוג קואורדינטות (x2, y2).
    :return: המרחק בין הנקודות.
    """
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


def avoid_collision(planes: List[CrazyPlane]) -> None:
    """
    מניעת התנגשויות
    מזהה ומתקן התנגשויות בין מטוסים באמצעות הזזתם לתאים סמוכים.

    :param planes: רשימת מטוסים לבדיקה.
    """
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
                    # העברת המטוס למשבצת סמוכה
                    possible_moves = plane_position.get_possible_moves_in_boundaries(CRAZY_STEP,
                                                                                     (MIN_CELL, MAX_CELL),
                                                                                     (MIN_CELL, MAX_CELL))
                    if possible_moves:
                        new_position = random.choice(possible_moves)
                        print(f"turn {plane} to {new_position}")
                        plane.goto(new_position)  # שימוש ב-unpacking לשליחת זוג פרמטרים
                        collision_detected = True


def main() -> None:
    """
    מדמה משחק שבו מטוסים זזים באופן רנדומלי בלוח דו-ממדי, נמנעים מהתנגשויות, ומדווחים על מצבם.

    המשחק מתנהל במשך מספר סבבים מוגדר, וכל סבב מעדכן את מיקומי המטוסים ובודק התנגשויות.
    """
    try:
        # יצירת מטוסים
        planes = allocate_planes_on_game_board(NUMBER_OF_PLANES)
        game_round = 1
        while game_round < ROUNDS + 1:
            print("-" * 10, f"round {game_round}", "-" * 10)
            game_round += 1
            # עדכון מיקום המטוסים
            for plane in planes:
                plane.update_position()

            # בדיקה למניעת התנגשויות
            avoid_collision(planes)

            # הדפסת מיקומי המטוסים
            print("\n".join(str(plane) for plane in planes))

            # המתנה של שנייה אחת לפני הלולאה הבאה
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        print("Game ended")


if __name__ == "__main__":
    main()

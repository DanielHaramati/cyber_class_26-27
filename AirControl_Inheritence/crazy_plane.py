import random
from position import Position


MIN_CELL, MAX_CELL = 0, 9   # גבולות המשחק (מערכת קואורדינטות 0 עד 9)
CRAZY_STEP = 1  # מספר תאים שהמטוס יכול לזוז בכל צעד

class CrazyPlane:
    """
    מחלקה לייצוג מטוס משוגע
    מטוס זז בתוך לוח דו-ממדי עם תנועות רנדומליות.

    מאפיינים:
        __x: הקואורדינטה האופקית של המטוס.
        __y: הקואורדינטה האנכית של המטוס.
        __name: שם או מזהה המטוס.
    """

    def __init__(self, position=None, name=None):
        """
        אתחול המטוס עם מיקום ושם.
        """
        self.__position = position
        self.__name = name

    def update_position(self) -> None:
        """
        מעדכן את מיקום המטוס באמצעות תנועה רנדומלית, תוך שמירה על גבולות המשחק.
        """
        self.__position.move_random_in_boundaries(CRAZY_STEP, (MIN_CELL, MAX_CELL), (MIN_CELL, MAX_CELL))


    def goto(self, new_position) -> None:
        """
        מעביר את המטוס למיקום חדש.
        """
        new_x = new_position.get_x()
        new_y = new_position.get_y()
        self.__position.goto_position_in_boundaries(new_x, new_y, (MIN_CELL, MAX_CELL), (MIN_CELL, MAX_CELL))

    def get_position(self) :
        """
        מחזיר את המיקום הנוכחי של המטוס.
        """
        return self.__position

    def __str__(self) -> str:
        """
        מציג את שם ומיקום המטוס בצורה טקסטואלית.

        :return: מחרוזת שמתארת את המטוס.
        """
        return f"plane: {self.__name} {self.__position}"

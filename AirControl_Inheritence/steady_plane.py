from plane import Plane


class SteadyPlane(Plane):
    def __init__(self, position=None, name=None):
        super().__init__(position, name)
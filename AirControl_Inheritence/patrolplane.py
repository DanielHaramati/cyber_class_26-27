from plane import Plane

class PatrolPlane(Plane):
    def __init__(self,pos,name , path):
        super.__init__(pos, name)
        self.__path = path
        self.__current_index = 0



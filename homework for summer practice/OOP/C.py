class BaseObject:
    def __init__(self, x, y ,z) -> None:
        self.x = x
        self.y = y
        self.z = z


    def get_coordinates(self) -> list:
        return self.x, self.y, self.z


class Block(BaseObject):
    def shatter(self) -> None:
        self.x = self.y = self.z = None


class Entity(BaseObject):
    def move(self, x, y, z) -> None:
        self.__init__(x, y, z)


class Thing(BaseObject):
    pass



def main():
    object = Block(1, 2, 5)
    object.shatter()

    print(object.get_coordinates())



main()
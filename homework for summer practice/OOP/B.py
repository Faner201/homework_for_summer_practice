from types import coroutine
from math import sqrt


class Vector2:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    
    def __add__(self,other):
        coordinate_x = self.x + other.x
        coordinate_y = self.y + other.y
        return Vector2(coordinate_x, coordinate_y)

    
    def __sub__(self, other):
        coroutine_x = self.x - other.x
        coroutine_y = self.y - other.y
        return Vector2(coroutine_x, coroutine_y)


    def __mul__(self, number):
        coordinate_x = self.x * number
        coordinate_y = self.y * number
        return Vector2(coordinate_x, coordinate_y)


    def __str__(self):
        return 'Vector2({}, {})'.format(self.x, self.y)

    
    def __eq__(self, other):
        if(self.x == other.x and self.y == other.y):
            return True
        else:
            return False


    def __abs__(self):
        return sqrt(self.x * self.x + self.y * self.y)


def main():

    vec1 = Vector2(3, 5)
    vec2 = Vector2(3, 5)
    vec_sum = vec1 == vec2
    print(vec_sum)


main()

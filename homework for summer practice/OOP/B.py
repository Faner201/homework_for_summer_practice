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


    def __rmul__(self, number):
        return self.__mul__(number)


    def __imul__(self, number):
        self.x *= number
        self.y *= number
        return self


    def __str__(self):
        return 'Vector2({}, {})'.format(self.x, self.y)

    
    def __eq__(self, other):
        if(self.x == other.x and self.y == other.y):
            return True
        else:
            return False

    
    def __ne__(self, other):
        return not self.__eq__(other)


    def __abs__(self):
        return sqrt(self.x * self.x + self.y * self.y)


def main():

    vec1 = Vector2(7, 6)
    vec2 = Vector2(-4, 2)
    print(vec1 + vec2)
    print(vec1 - vec2)
    print(vec1 * 2)
    print(7 * vec2)
    vec2 *= 5
    print(vec1 == vec2)
    print(vec1 != vec2)
    print(abs(vec1))


main()

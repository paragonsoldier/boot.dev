class Rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_area(self):
        return self._length * self._width

    def get_perimeter(self):
        return 2 * self._length + 2 * self._width


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


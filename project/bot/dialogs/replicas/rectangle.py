from .base import DialogReplica


class Rectangle(DialogReplica):
    length: int
    width: int

    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __str__(self):
        return 'Прямоугольник %dx%d' % (self.length, self.width)

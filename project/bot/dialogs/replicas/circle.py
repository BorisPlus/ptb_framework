from .base import DialogReplica


class Circle(DialogReplica):
    radius: int

    def __init__(self, radius: int):
        self.radius = radius

    def __str__(self):
        return f"Круг R={self.radius}"

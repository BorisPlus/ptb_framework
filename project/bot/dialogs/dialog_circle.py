from .common import get_int
from .replicas import Circle


def dialog_circle():
    _ = yield ''  # Строка обязательна. Фича.
    radius: int = yield from get_int("Введите радиус", "./project/img/circle.png")
    yield Circle(radius=radius)

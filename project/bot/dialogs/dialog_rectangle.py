from .common import get_int
from .replicas import Rectangle


def dialog_rectangle():
    _ = yield ''  # Строка обязательна. Фича.
    length: int = yield from get_int("Введите длину", "./project/img/rectangle.jpg")
    width: int = yield from get_int("Введите ширину", "./project/img/rectangle.jpg")
    yield Rectangle(length=length, width=width)

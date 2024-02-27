import typing

from ui.buttons.base import CallbackDataButton


class RectanglePerimeter(CallbackDataButton):
    action: str = "rectangle_perimeter"
    title: str = "Рассчитать периметр прямоугольника"
    length: int
    width: int

    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def get_callback_data(self) -> typing.Tuple[str]:
        return f"{self.length}", f"{self.width}"

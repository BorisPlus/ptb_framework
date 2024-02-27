import typing

from ui.buttons.base import CallbackDataButton


class RectangleArea(CallbackDataButton):
    action: str = "rectangle_area"
    title: str = "Рассчитать площадь прямоугольника"
    length: int
    width: int

    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def get_callback_data(self) -> typing.Tuple[str]:
        return f"{self.length}", f"{self.width}"

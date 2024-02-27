import typing

from ui.buttons.base import CallbackDataButton


class CircleArea(CallbackDataButton):
    action: str = "circle_area"
    title: str = "Рассчитать площадь круга"
    radius: int

    def __init__(self, radius: int):
        self.radius = radius

    def get_callback_data(self) -> typing.Tuple[str]:
        return f"{self.radius}",

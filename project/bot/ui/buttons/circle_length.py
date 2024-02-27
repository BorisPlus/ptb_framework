import typing

from ui.buttons.base import CallbackDataButton


class CircleLength(CallbackDataButton):
    action: str = "circle_length"
    title: str = "Рассчитать длину окружности"
    radius: int

    def __init__(self, radius: int):
        self.radius = radius

    def get_callback_data(self) -> typing.Tuple[str]:
        return f"{self.radius}",

from telegram import Update

from .replicas import ImageWithCaption


def get_int(request: str, image_file_path: str):
    response: Update = yield ImageWithCaption(image_file_path, request)
    value = 0
    while True:
        if response.message.text.isdigit():
            if int(response.message.text) <= 100:
                value = int(response.message.text)
                break
            else:
                additional = "Должно быть не больше 100"
        else:
            additional = "Должно быть целочисленное"
        response: Update = yield ImageWithCaption(image_file_path, f"{additional}. {request}")
    return value

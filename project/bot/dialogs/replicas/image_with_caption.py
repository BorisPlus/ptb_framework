from .base import DialogReplica


class ImageWithCaption(DialogReplica):
    image_file_path: str
    caption: str

    def __init__(self, image_file_path: int, caption: int):
        self.image_file_path = image_file_path
        self.caption = caption

    def __str__(self):
        return '%s: %s' % (self.view(), self.caption)

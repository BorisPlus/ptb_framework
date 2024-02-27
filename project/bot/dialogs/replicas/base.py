import re

pattern = re.compile(r'(?<!^)(?=[A-Z])')


class DialogReplica:

    @classmethod
    def view(cls) -> str:
        return pattern.sub('_', cls.__name__).lower()

    def __init__(self, *args, **kwargs):
        ...

    def __str__(self):
        return self.view

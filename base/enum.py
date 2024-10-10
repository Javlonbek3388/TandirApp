from enum import Enum


class Tillar(Enum):
    PYTHON = 'Python',
    JAVASCRIPT = 'Java Scripts',
    JAVA = 'Java',

    @classmethod
    def choices(cls):
        return tuple((key.value, key.name) for key in cls)


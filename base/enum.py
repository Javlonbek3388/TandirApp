from enum import Enum


class Tillar(Enum):
    PYTHON = 'Python'
    JAVASCRIPT = 'JavaScript'
    JAVA = 'Java'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

from .Type import *


class Symbol:
    def __init__(self, name: str, offset: int, type: AbstractType):
        # 变量名
        self.name = name
        # 相对于fp的偏移
        self.offset = offset
        self.type = type

    def __str__(self):
        return self.name + "@" + str(self.type) + ":" + str(self.offset)

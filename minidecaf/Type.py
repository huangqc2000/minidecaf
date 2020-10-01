from abc import ABCMeta, abstractmethod


class AbstractType(object):
    __metaclass__ = ABCMeta

    def __init__(self, name) -> None:
        self.name = name

    @abstractmethod
    def equals(self, type) -> bool: pass

    def __str__(self):
        return self.name

    # 类型所占内存空间的大小
    @abstractmethod
    def getSize(self) -> int: pass


# 没有类型的数节点
class NoType(AbstractType):
    def __init__(self) -> None:
        super().__init__("NoType")

    def equals(self, type) -> bool:
        return isinstance(type, NoType)

    def getSize(self) -> int:
        raise Exception("Error: trying getting the size of NoType.")


# 整形
class IntType(AbstractType):
    def __init__(self) -> None:
        super().__init__("IntType")

    def equals(self, type) -> bool:
        return isinstance(type, IntType)

    def getSize(self) -> int:
        return 4

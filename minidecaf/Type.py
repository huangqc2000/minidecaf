
class Type:
    def __init__(self, name) -> None:
        self.name = name
    def equals(self, type) -> bool:
        return True

# 没有类型的数节点
class NoType(Type):
    def __init__(self) -> None:
        super().__init__("NoType")

    def equals(self, type) -> bool:
        return isinstance(type,NoType)

# 整形
class IntType(Type):
    def __init__(self) -> None:
        super().__init__("IntType")

    def equals(self, type) -> bool:
        return isinstance(type,IntType);



from .Type import *


class FunType:
    def __init__(self, returnType: AbstractType, paramTypes: list) -> None:
        self.returnType = returnType
        self.paramTypes = paramTypes

    # 返回类型相同 参数类型相同
    def equals(self, funType) -> bool:
        if not self.returnType.equals(funType.returnType):
            return False
        if len(self.paramTypes) != len(funType.paramTypes):
            return False
        for i in range(len(self.paramTypes)):
            if not self.paramTypes[i].equals(funType.paramTypes[i]):
                return False
        return True

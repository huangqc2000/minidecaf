from enum import Enum


class ValueCat(Enum):
    Lvalue = 0
    Rvalue = 1


class AbstractType(object):

    def __init__(self, name, valueCat=ValueCat.Rvalue) -> None:
        self.name = name
        self.valueCat = valueCat

    def equals(self, ty) -> bool: pass

    def __str__(self):
        return f"{self.name} ( {self.valueCat} )"

    # 取地址
    def referenced(self): pass

    # 解引用
    def dereferenced(self): pass

    # 左右值转化
    def valueCast(self, targetValueCat): pass

    # 类型所占内存空间的大小
    def getSize(self) -> int: pass


# 没有类型的数节点
class NoType(AbstractType):
    def __init__(self) -> None:
        super().__init__("NoType")

    def equals(self, ty) -> bool:
        return isinstance(ty, NoType)

    def getSize(self) -> int:
        raise Exception("Error: trying to get the size of NoType.")

    def referenced(self):
        raise Exception("Error: trying to referencing of NoType")

    def dereferenced(self):
        raise Exception("Error: trying to dereferencing of NoType")

    def valueCast(self, targetValueCat):
        return self


# 整形
class IntType(AbstractType):
    def __init__(self, valueCat=ValueCat.Rvalue) -> None:
        super().__init__("IntType", valueCat)

    def equals(self, ty) -> bool:
        return isinstance(ty, IntType) and self.valueCat == ty.valueCat

    def getSize(self) -> int:
        return 4

    def referenced(self):
        if self.valueCat == ValueCat.Lvalue:
            return PointerType(1)
        else:
            raise Exception("Error: trying to referencing a rvalue of int")

    def dereferenced(self):
        raise Exception("Error: trying to dereferencing a int")

    def valueCast(self, targetValueCat):
        return IntType(targetValueCat)


# 指针类型
class PointerType(AbstractType):
    def __init__(self, starNum, valueCat=ValueCat.Rvalue):
        super().__init__("PointerType", valueCat)
        self.starNum = starNum  # *个数

    def equals(self, ty) -> bool:
        return isinstance(ty, PointerType) and self.starNum == ty.starNum and self.valueCat == ty.valueCat

    def getSize(self) -> int:
        return 4

    def referenced(self):
        if self.valueCat == ValueCat.Lvalue:
            return PointerType(self.starNum + 1)
        else:
            raise Exception("Error: trying to referencing a rvalue of pointer")

    def dereferenced(self):
        if self.starNum > 1:
            return PointerType(self.starNum - 1, ValueCat.Lvalue)
        else:
            return IntType(ValueCat.Lvalue)

    def valueCast(self, targetValueCat):
        return PointerType(self.starNum, targetValueCat)
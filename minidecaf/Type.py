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
        raise Exception("trying to get the size of NoType.")

    def referenced(self):
        raise Exception("trying to referencing of NoType")

    def dereferenced(self):
        raise Exception("trying to dereferencing of NoType")

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
            raise Exception("trying to referencing a rvalue of int")

    def dereferenced(self):
        raise Exception("trying to dereferencing a int")

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
            raise Exception("trying to referencing a rvalue of pointer")

    def dereferenced(self):
        if self.starNum > 1:
            return PointerType(self.starNum - 1, ValueCat.Lvalue)
        else:
            return IntType(ValueCat.Lvalue)

    def valueCast(self, targetValueCat):
        return PointerType(self.starNum, targetValueCat)


class ArrayType(AbstractType):
    def __init__(self, baseType, length):
        super().__init__("ArrayType")
        self.baseType = baseType
        self.length = length
        self.size = length * self.baseType.getSize()

    def equals(self, ty) -> bool:
        return isinstance(ty, ArrayType) and self.size == ty.getSize() and self.baseType.equals(ty.baseType)

    def referenced(self):
        raise Exception("trying to referencing a array")

    def dereferenced(self):
        raise Exception("trying to dereferencing a array")

    def valueCast(self, targetValueCat):
        if targetValueCat == ValueCat.Lvalue:
            raise Exception("array must be a Rvalue")
        else:
            return ArrayType(self.baseType, self.length)

    def getSize(self) -> int:
        return self.size

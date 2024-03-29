from .generated.MiniDecafLexer import MiniDecafLexer
from .generated.MiniDecafParser import MiniDecafParser
from .generated.MiniDecafVisitor import MiniDecafVisitor
from .utils import *
from .Symbol import *
from .FunType import *


class MainVisitor(MiniDecafVisitor):
    def __init__(self):
        self.asm = []
        self.containsMain = False
        # 局部变量个数
        self.localCount = 0

        self.currentFunc = ""
        # 符号表 栈 list[{name:Symbol}]
        self.symbolTable = []
        # 条件语句和条件表达式所用label编号
        self.condNo = 0
        # 循环label编号
        self.loopNo = 0
        # 当前位置的循环编号 栈
        self.loopNos = []
        # 声明函数
        self.declaredFuncTable = {}
        # 定义函数
        self.definedFuncTable = {}
        # (name)String:Type
        self.declaredGlobalTable = {}
        # (name)Stirng:Type
        self.initializedGlobalTable = {}

    def visitProg(self, ctx: MiniDecafParser.ProgContext):
        # for child in ctx.children:
        #     self.visit(child)
        # visit child
        self.visitChildren(ctx)
        # 将未初始化的全局变量发送到 bss 段
        self.asm.insert(0, "\t.bss\n")
        for globalIdent in self.declaredGlobalTable.keys():
            if self.initializedGlobalTable.get(globalIdent) is None:
                self.asm.insert(1, "\t.comm " + globalIdent + ", " +
                                str(self.declaredGlobalTable.get(globalIdent).getSize()) + ", 4\n")  # 大小为 4，对齐字节数也为 4

        if not self.containsMain:
            raise Exception("main function not found")

        return NoType()

    def visitDeclaredFunc(self, ctx: MiniDecafParser.DeclaredFuncContext):
        funcName = ctx.Ident(0).getText()
        if self.declaredGlobalTable.get(funcName) is not None:
            raise Exception("same name for a global v and a func")

        returnType = self.visit(ctx.ty(0))
        paramTypes = []
        for i in range(1, len(ctx.ty())):
            paramTypes.append(self.visit(ctx.ty(i)))
        funType = FunType(returnType, paramTypes)
        # 如果声明过但签名不同 报错
        if self.declaredFuncTable.get(funcName) is not None and not self.declaredFuncTable.get(funcName).equals(
                funType):
            raise Exception("declare a function with two different signatures")

        self.declaredFuncTable[funcName] = funType
        return NoType()

    def visitDefinedFunc(self, ctx: MiniDecafParser.DefinedFuncContext):
        self.currentFunc = ctx.Ident(0).getText()
        if self.declaredGlobalTable.get(self.currentFunc) is not None:
            raise Exception("same name for a global v and a func")
        if self.currentFunc == "main":
            self.containsMain = True
        self.asm.extend(["\t.text\n", "\t.global " + self.currentFunc + "\n", self.currentFunc + ":\n"])
        if self.definedFuncTable.get(self.currentFunc, None) is not None:
            raise Exception("define two functions as a same name")

        returnType = self.visit(ctx.ty(0))
        paramTypes = []
        for i in range(1, len(ctx.ty())):
            paramTypes.append(self.visit(ctx.ty(i)))
        funType = FunType(returnType, paramTypes)

        if self.declaredFuncTable.get(self.currentFunc) is not None and not self.declaredFuncTable.get(
                self.currentFunc).equals(funType):
            raise Exception("the signature of the defined function is not the same as declared")
        # 加入declaredFuncTable和definedFuncTable中
        self.declaredFuncTable[self.currentFunc] = funType
        self.definedFuncTable[self.currentFunc] = funType

        self.assignStackFrame()
        # 记录当前位置 之后要插入
        backtracePos = len(self.asm)
        self.localCount = 0
        # 为这个函数体开启一个新的作用域
        self.symbolTable.append({})

        # 将函数的参数作为局部变量取出
        for i in range(1, len(ctx.Ident())):
            paraName = ctx.Ident(i).getText()
            if self.symbolTable[-1].get(paraName, None) is not None:
                raise Exception("two param have the same name")
            if i < 9:
                self.localCount += 1
                # 通过寄存器传参 a0-a7
                self.asm.append("\tsw a" + str(i - 1) + ", " + str(-4 * i) + "(fp)\n")
                # 参数转化为左值
                self.symbolTable[-1][paraName] = Symbol(paraName, -4 * i,
                                                        funType.paramTypes[i - 1].valueCast(ValueCat.Lvalue))
            else:
                self.symbolTable[-1][paraName] = Symbol(paraName, 4 * (i - 9 + 2),
                                                        funType.paramTypes[i - 1].valueCast(ValueCat.Lvalue))

        # 发射函数体
        for blockItem in ctx.blockItem():
            self.visit(blockItem)
        # 关闭作用域
        self.symbolTable.pop()

        # 默认返回0
        self.asm.extend(["# return 0 as default\n", "\tli t1, 0\n", "\taddi sp, sp, -4\n", "\tsw t1, 0(sp)\n"])
        # 分配局部变量空间
        self.asm.insert(backtracePos,
                        "# assign stack to store local variable\n\taddi sp, sp, " + str(-4 * self.localCount) + "\n")

        # 恢复栈帧
        self.recoverStackFrame()

        return NoType()

    def visitGlobalIntOrPointerDecl(self, ctx: MiniDecafParser.GlobalIntOrPointerDeclContext):
        # 全局变量可以多次声明，但只能被初始化一次
        name = ctx.Ident().getText()
        if self.declaredFuncTable.get(name) is not None:
            raise Exception("same name for a global v and a func")

        ty = self.visit(ctx.ty())
        if self.declaredGlobalTable.get(name) is not None and not self.declaredGlobalTable.get(name).equals(ty):
            raise Exception("global variables with different type")

        self.declaredGlobalTable[name] = ty.valueCast(ValueCat.Lvalue)

        if ctx.Integer() is not None:
            if self.initializedGlobalTable.get(name) is not None:
                raise Exception("initializing a global variable twice")
            self.initializedGlobalTable[name] = ty.valueCast(ValueCat.Lvalue)
            self.asm.append("\t.data\n")
            self.asm.append("\t.align 4\n")
            self.asm.append(name + ":\n")
            self.asm.append("\t.word " + ctx.Integer().getText() + "\n")

        return NoType()

    def visitGlobalArrayDecl(self, ctx: MiniDecafParser.GlobalArrayDeclContext):
        name = ctx.Ident().getText()
        if self.declaredFuncTable.get(name) is not None:
            raise Exception("same name for a global array and a func")
        types = []
        types.append(self.visit(ctx.ty()).valueCast(ValueCat.Lvalue))
        for i in range(len(ctx.Integer()) - 1, -1, -1):
            dim = int(ctx.Integer(i).getText())
            if dim > INT_MAX or dim <= 0:
                raise Exception(f"wrong dimension {i - 1} of array")
            types.insert(0, ArrayType(types[0], dim))
        ty = types[0]
        if self.declaredGlobalTable.get(name) is not None and not self.declaredGlobalTable.get(name).equals(ty):
            raise Exception("array declared differently with global declare")
        self.declaredGlobalTable[name] = ty
        return NoType()

    def visitLocalIntOrPointerDecl(self, ctx: MiniDecafParser.LocalIntOrPointerDeclContext):
        name = ctx.Ident().getText()
        # 已经声明过了
        if self.symbolTable[-1].__contains__(name):
            raise Exception("Repeated statement for" + name)
        # 加入符号表
        ty = self.visit(ctx.ty())
        self.localCount += 1
        self.symbolTable[-1][name] = Symbol(name, -4 * self.localCount, ty.valueCast(ValueCat.Lvalue))
        # 初始化
        if ctx.expr() is not None:
            # self.visit(ctx.expr())
            exprType = self.RValueCast(self.visit(ctx.expr()))
            if not exprType.equals(ty):
                raise Exception(f"initialize value of type  {exprType.name} to some variable of type {ty.name}")
            self.pop("t0")
            self.asm.append("# assignment for local variable " + name + "\n")
            self.asm.append("\tsw t0, " + str(-4 * self.localCount) + "(fp)\n")

        return NoType()

    def visitLocalArrayDecl(self, ctx: MiniDecafParser.LocalArrayDeclContext):
        name = ctx.Ident().getText()
        # 已经声明过了
        if self.symbolTable[-1].__contains__(name):
            raise Exception("Repeated statement for" + name)
        types = []
        types.append(self.visit(ctx.ty()).valueCast(ValueCat.Lvalue))
        for i in range(len(ctx.Integer())-1, -1, -1):
            dim = int(ctx.Integer(i).getText())
            if dim <= 0 or dim > INT_MAX:
                raise Exception(f"wrong dimension {i - 1} of array")
            types.insert(0, ArrayType(types[0], dim))
        # ???
        # assert isinstance(types[0], ArrayType)
        ty = types[0]
        # 数组相当于多个变量
        self.localCount += int(ty.getSize() / 4)
        self.symbolTable[-1][name] = Symbol(name, -4 * self.localCount, ty)

    def visitExprStmt(self, ctx: MiniDecafParser.ExprStmtContext):
        expr = ctx.expr()
        if expr is not None:
            # 表达式不会再使用
            self.visit(expr)
            # 例如a=1+2 会返回3 此时应该pop出来
            self.pop("t0")

        return NoType()

    def visitReturnStmt(self, ctx: MiniDecafParser.ReturnStmtContext):
        returnType = self.RValueCast(self.visit(ctx.expr()))
        expectedType = self.definedFuncTable.get(self.currentFunc).returnType
        if not expectedType.equals(returnType):
            raise Exception(f"expect return type {expectedType.name}, found {returnType.name}")
        # 函数返回 返回值在栈顶
        self.asm.append("\tj .exit." + self.currentFunc + "\n")
        return NoType()

    def visitIfStmt(self, ctx: MiniDecafParser.IfStmtContext):
        currentCondNo = str(self.condNo)
        self.condNo += 1
        self.asm.append("# # if\n")  # 多一个#
        # 获得表达式的值
        self.checkType(self.visit(ctx.expr()), "IntType")
        self.pop("t0")
        self.asm.append("\tbeqz t0, .else" + currentCondNo + "\n")
        self.visit(ctx.stmt(0))
        self.asm.append("\tj .afterCond" + currentCondNo + "\n")
        self.asm.append(".else" + currentCondNo + ":\n")
        if len(ctx.stmt()) > 1:
            self.visit(ctx.stmt(1))
        self.asm.append(".afterCond" + currentCondNo + ":\n")
        return NoType()

    def visitBlockStmt(self, ctx: MiniDecafParser.BlockStmtContext):
        self.symbolTable.append({})
        for blockItem in ctx.blockItem():
            self.visit(blockItem)
        self.symbolTable.pop()
        return NoType()

    def visitWhileStmt(self, ctx: MiniDecafParser.WhileStmtContext):
        currentLoopNo = self.increaseLoopNo()
        self.asm.append("# while\n")
        self.asm.append(".beforeLoop" + currentLoopNo + ":\n")
        self.asm.append(".continueLoop" + currentLoopNo + ":\n")
        self.checkType(self.visit(ctx.expr()), "IntType")
        self.pop("t0")
        self.asm.append("\tbeqz t0, .afterLoop" + currentLoopNo + "\n")
        # 访问循环体
        self.loopNos.append(currentLoopNo)
        self.visit(ctx.stmt())
        self.loopNos.pop()

        self.asm.append("\tj .beforeLoop" + currentLoopNo + "\n")
        self.asm.append(".afterLoop" + currentLoopNo + ":\n")
        return NoType()

    def visitForStmt(self, ctx: MiniDecafParser.ForStmtContext):
        currentLoopNo = self.increaseLoopNo()
        self.asm.append("# for\n")

        # 取出for循环中的表达式
        initExpr = None
        condExpr = None
        afterExpr = None
        for i in range(len(ctx.children)):
            if isinstance(ctx.children[i], MiniDecafParser.ExprContext):
                expr = ctx.children[i]
                if ctx.children[i - 1].getText() == "(":
                    initExpr = expr
                elif ctx.children[i + 1].getText() == ";":
                    condExpr = expr
                else:
                    afterExpr = expr
        # 开一个新的作用域 for小括号里面
        self.symbolTable.append({})
        if initExpr is not None:
            self.visit(initExpr)
            self.addsp(1)
        if ctx.localDecl() is not None:
            self.visit(ctx.localDecl())

        self.asm.append(".beforeLoop" + currentLoopNo + ":\n")
        if condExpr is not None:
            self.checkType(self.visit(condExpr), "IntType")
            self.asm.append("\tlw t1, 0(sp)\n")
            self.asm.append("\taddi sp, sp, 4\n")
            self.asm.append("\tbeqz t1, .afterLoop" + currentLoopNo + "\n")

        # 访问循环体
        self.loopNos.append(currentLoopNo)
        # ???
        # self.symbolTable.append({})
        self.visit(ctx.stmt())
        # self.symbolTable.pop()
        self.loopNos.pop()

        self.asm.append(".continueLoop" + currentLoopNo + ":\n")
        if afterExpr is not None:
            self.visit(afterExpr)
            self.addsp(1)
        self.symbolTable.pop()

        self.asm.append("\tj .beforeLoop" + currentLoopNo + "\n")
        self.asm.append(".afterLoop" + currentLoopNo + ":\n")
        return NoType()

    def visitDoStmt(self, ctx: MiniDecafParser.DoStmtContext):
        currentLoopNo = self.increaseLoopNo()
        self.asm.append("# do-while\n")

        self.asm.append(".beforeLoop" + currentLoopNo + ":\n")
        self.loopNos.append(currentLoopNo)
        self.visit(ctx.stmt())
        self.loopNos.pop()

        self.asm.append(".continueLoop" + currentLoopNo + ":\n")
        self.checkType(self.visit(ctx.expr()), "IntType")
        self.pop("t0")
        self.asm.append("\tbnez t0, .beforeLoop" + currentLoopNo + "\n")
        self.asm.append(".afterLoop" + currentLoopNo + ":\n")

        return NoType()

    def visitBreakStmt(self, ctx: MiniDecafParser.BreakStmtContext):
        if len(self.loopNos) == 0:
            raise Exception("break statement not within loop")
        self.asm.append("\tj .afterLoop" + self.loopNos[-1] + "\n")
        return NoType()

    def visitContinueStmt(self, ctx: MiniDecafParser.ContinueStmtContext):
        if len(self.loopNos) == 0:
            raise Exception("continue statement not within loop")
        self.asm.append("\tj .continueLoop" + self.loopNos[-1] + "\n")
        return NoType()

    def visitExpr(self, ctx: MiniDecafParser.ExprContext):
        if len(ctx.children) > 1:
            unaryType = self.visit(ctx.unary())
            if unaryType.valueCat == ValueCat.Rvalue:
                raise Exception("expect lvalue, but found rvalue")
            # ???
            # unaryType = unaryType.valueCast(ValueCat.Lvalue)
            exprType = self.RValueCast(self.visit(ctx.expr()))
            if not exprType.equals(unaryType.valueCast(ValueCat.Rvalue)):
                raise Exception("assign value of type is not the same as the variable type")
            self.pop("t1")
            self.pop("t0")
            self.asm.append(("# assign\n"
                             "\tsw t1, 0(t0)\n"
                             ))
            self.push("t0")
            return unaryType
        else:
            return self.visit(ctx.ternary())

    def visitTernary(self, ctx: MiniDecafParser.TernaryContext):
        if len(ctx.children) > 1:
            currentCondNo = str(self.condNo)
            self.condNo += 1
            self.asm.append("# ternary conditional\n")
            self.checkType(self.visit(ctx.lor()), "IntType")
            self.pop("t0")
            self.asm.append("\tbeqz t0, .else" + currentCondNo + "\n")
            thenType = self.RValueCast(self.visit(ctx.expr()))
            self.asm.append("\tj .afterCond" + currentCondNo + "\n")
            self.asm.append(".else" + currentCondNo + ":\n")
            elseType = self.RValueCast(self.visit(ctx.ternary()))
            self.asm.append(".afterCond" + currentCondNo + ":\n")
            if not thenType.equals(elseType):
                raise Exception("a ternary has to different return types")
            return thenType
        else:
            return self.visit(ctx.lor())

    def visitLor(self, ctx: MiniDecafParser.LorContext):
        if len(ctx.children) > 1:
            leftType = self.checkType(self.visit(ctx.lor(0)), "IntType")
            rightType = self.checkType(self.visit(ctx.lor(1)), "IntType")
            if isinstance(leftType, ArrayType) or isinstance(rightType, ArrayType):
                raise Exception("array cannot or")
            self.pop("t1")
            self.pop("t0")
            self.asm.append(RulesToAsm["||"])
            self.push("t0")
            return IntType()
        else:
            return self.visit(ctx.land())

    def visitLand(self, ctx: MiniDecafParser.LandContext):
        if len(ctx.children) > 1:
            leftType = self.checkType(self.visit(ctx.land(0)), "IntType")
            rightType = self.checkType(self.visit(ctx.land(1)), "IntType")
            if isinstance(leftType, ArrayType) or isinstance(rightType, ArrayType):
                raise Exception("array cannot and")
            self.pop("t1")
            self.pop("t0")
            self.asm.append(RulesToAsm["&&"])
            self.push("t0")
            return IntType()
        else:
            return self.visit(ctx.equ())

    def visitEqu(self, ctx: MiniDecafParser.EquContext):
        if len(ctx.children) > 1:
            leftType = self.RValueCast(self.visit(ctx.equ(0)))
            rightType = self.RValueCast(self.visit(ctx.equ(1)))
            if not leftType.equals(rightType):
                raise Exception("type between equ must be the same")
            # ???
            if isinstance(leftType, ArrayType) or isinstance(rightType, ArrayType):
                raise Exception("array cannot equ")
            self.pop("t1")
            self.pop("t0")
            op = ctx.children[1].getText()
            tmpAsm = RulesToAsm.get(op, None)
            if tmpAsm is None:
                raise Exception("equ rules error")
            self.asm.append(tmpAsm)
            self.push("t0")
            return IntType()
        else:
            return self.visit(ctx.rel())

    def visitRel(self, ctx: MiniDecafParser.RelContext):
        if len(ctx.children) > 1:
            leftType = self.checkType(self.visit(ctx.rel(0)), "IntType")
            rightType = self.checkType(self.visit(ctx.rel(1)), "IntType")
            if isinstance(leftType, ArrayType) or isinstance(rightType, ArrayType):
                raise Exception("array cannot rel")
            self.pop("t1")
            self.pop("t0")
            op = ctx.children[1].getText()
            tmpAsm = RulesToAsm.get(op, None)
            if tmpAsm is None:
                raise Exception("rel rules error")
            self.asm.append(tmpAsm)
            self.push("t0")
            return IntType()
        else:
            return self.visit(ctx.add())

    def visitAdd(self, ctx: MiniDecafParser.AddContext):
        if len(ctx.children) > 1:
            leftType = self.RValueCast(self.visit(ctx.add(0)))
            rightType = self.RValueCast(self.visit(ctx.add(1)))
            if isinstance(leftType, ArrayType) or isinstance(rightType, ArrayType):
                raise Exception("array cannot add")
            op = ctx.children[1].getText()
            if op == "+":
                self.pop("t1")
                self.pop("t0")
                if isinstance(leftType, IntType) and isinstance(rightType, IntType):
                    self.asm += RulesToAsm.get(op, None)
                    self.push("t0")
                    return IntType()
                elif isinstance(leftType, PointerType) and isinstance(rightType, IntType):
                    self.asm.append(("# pointer + int\n"
                                     "\tslli t1, t1, 2\n"
                                     "\tadd t0, t0, t1\n"
                                     ))
                    self.push("t0")
                    return leftType
                elif isinstance(leftType, IntType) and isinstance(rightType, PointerType):
                    self.asm.append(("# int + pointer\n"
                                     "\tslli t0, t0, 2\n"
                                     "\tadd t0, t0, t1\n"
                                     ))
                    self.push("t0")
                    return rightType
                else:
                    raise Exception("pointer can not add pointer")
            else:
                self.pop("t1")
                self.pop("t0")
                if isinstance(leftType, IntType) and isinstance(rightType, IntType):
                    self.asm += RulesToAsm.get(op, None)
                    self.push("t0")
                    return IntType()
                elif isinstance(leftType, PointerType) and isinstance(rightType, IntType):
                    self.asm.append(("# pointer - int\n"
                                     "\tslli t1, t1, 2\n"
                                     "\tsub t0, t0, t1\n"
                                     ))
                    self.push("t0")
                    return leftType
                elif isinstance(leftType, PointerType) and rightType.equals(leftType):
                    self.asm.append(("# pointer - pointer\n"
                                     "\tsub t0, t0, t1\n"
                                     "\tsrai t0, t0, 2\n"
                                     ))
                    self.push("t0")
                    return IntType()
                else:
                    raise Exception("pointer can not add pointer")
        else:
            return self.visit(ctx.mul())

    def visitMul(self, ctx: MiniDecafParser.MulContext):
        if len(ctx.children) > 1:
            leftType = self.checkType(self.visit(ctx.mul(0)), "IntType")
            rightType = self.checkType(self.visit(ctx.mul(1)), "IntType")
            if isinstance(leftType, ArrayType) or isinstance(rightType, ArrayType):
                raise Exception("array cannot mul")
            self.pop("t1")
            self.pop("t0")
            op = ctx.children[1].getText()
            tmpAsm = RulesToAsm.get(op, None)
            if tmpAsm is None:
                raise Exception("mul rules error")
            self.asm.append(tmpAsm)
            self.push("t0")
            return IntType()
        else:
            return self.visit(ctx.unary())

    def visitOpUnary(self, ctx: MiniDecafParser.OpUnaryContext):
        ty = self.visit(ctx.unary())
        op = ctx.children[0].getText()
        if op == "*":
            return self.RValueCast(ty).dereferenced()
        elif op == "&":
            return ty.referenced()
        else:
            self.checkType(ty, "IntType")
            self.pop("t0")
            # 特判一下 - 因为与减符号相同无法使用字典
            if op == "-":
                self.asm.append("# - int\n")
                self.asm.append("\tneg t0, t0\n")
            else:
                tmpAsm = RulesToAsm.get(op, None)
                if tmpAsm is None:
                    raise Exception("unary rules error")
                self.asm.append(tmpAsm)
            self.push("t0")
            return IntType()

    def visitCastUnary(self, ctx: MiniDecafParser.CastUnaryContext):
        srcType = self.visit(ctx.unary())
        dstType = self.visit(ctx.ty())
        return dstType.valueCast(srcType.valueCat)

    def visitPostfixUnary(self, ctx: MiniDecafParser.PostfixUnaryContext):
        return self.visit(ctx.postfix())

    def visitCallPostfix(self, ctx: MiniDecafParser.CallPostfixContext):
        name = ctx.Ident().getText()
        if self.declaredFuncTable.get(name, None) is None:
            raise Exception("try calling an undeclared function")
        funType = self.declaredFuncTable.get(name)
        if len(funType.paramTypes) != len(ctx.expr()):
            raise Exception("the number of arguments is not equal to the number of parameters")
        self.asm.append("# prepare arguments\n")
        for i in range(len(ctx.expr()) - 1, -1, -1):
            ty = self.RValueCast(self.visit(ctx.expr(i)))
            if not ty.equals(funType.paramTypes[i]):
                raise Exception(
                    f"the type of argument {i} is different from the type of parameter {i} of function {name}")
            if i < 8:
                self.pop("a" + str(i))
        self.asm.append("\tcall " + name + "\n")
        # 函数返回值在a0中
        self.push("a0")
        return funType.returnType

    def visitSubscriptPostfix(self, ctx: MiniDecafParser.SubscriptPostfixContext):
        postfixType = self.RValueCast(self.visit(ctx.postfix()))
        self.checkType(self.visit(ctx.expr()), "IntType")
        self.pop("t1")
        self.pop("t0")
        if isinstance(postfixType, PointerType):
            self.asm.append(("# subscript to a pointer\n"
                             "\tslli t1, t1, 2\n"
                             "\tadd t0, t0, t1\n"
                             ))
            self.push("t0")
            return postfixType.dereferenced()
        elif isinstance(postfixType, ArrayType):
            baseType = postfixType.baseType
            self.asm.append(("# subscript to an array\n"
                             f"\tli t2, {baseType.getSize()}\n"
                             "\tmul t1, t1, t2\n"
                             "\tadd t0, t0, t1\n"
                             ))
            self.push("t0")
            return baseType
        else:
            raise Exception(f"the subscript could not apply to a {postfixType.name}")

    def visitPrimaryPostfix(self, ctx: MiniDecafParser.PrimaryPostfixContext):
        return self.visit(ctx.primary())

    def visitNumPrimary(self, ctx: MiniDecafParser.NumPrimaryContext):
        if int(ctx.Integer().getText()) > INT_MAX:
            raise Exception("large number")

        self.asm.extend(["# number " + ctx.Integer().getText() + "\n",
                         "\tli t0, " + ctx.Integer().getText() + "\n"])
        self.push("t0")
        return IntType()

    def visitIdentPrimary(self, ctx: MiniDecafParser.IdentPrimaryContext):
        name = ctx.Ident().getText()
        symbol = self.lookupSymbol(name)
        if symbol is None:  # 全局 or 不存在
            if self.declaredGlobalTable.get(name) is not None:
                self.asm.append(f"# read global variable {name}\n")
                self.asm.append("\tla t0, " + name + "\n")
                self.push("t0")
                return self.declaredGlobalTable.get(name)
            else:
                raise Exception("variable {} is not defined".format(name))
        else:  # 局部
            self.asm.append((f"# read variable {name} as lvalue\n"
                             f"\taddi t0, fp, {symbol.offset} \n"))
            self.push("t0")
            return symbol.type

    def visitParenthesizedPrimary(self, ctx: MiniDecafParser.ParenthesizedPrimaryContext):
        return self.visit(ctx.expr())

    def visitTy(self, ctx: MiniDecafParser.TyContext):
        starNum = len(ctx.children) - 1
        if starNum == 0:
            return IntType()
        else:
            return PointerType(starNum)

    # return loopNo++
    def increaseLoopNo(self):
        currentLoopNo = str(self.loopNo)
        self.loopNo += 1
        return currentLoopNo

    def assignStackFrame(self):
        self.asm.append("# assign stack frame\n")
        self.push("ra")
        self.push("fp")
        self.asm.append("\tmv fp, sp\n")

    def recoverStackFrame(self):
        self.asm.extend(
            ["# recover stack frame\n", ".exit." + self.currentFunc + ":\n", "\tlw a0, 0(sp)\n", "\tmv sp, fp\n"])
        self.pop("fp")
        self.pop("ra")
        self.asm.append("\tret\n\n")

    def addsp(self, v: int):
        self.asm.append("\taddi sp, sp, " + str(v * 4) + "\n")

    # 类型检测并转化为右值
    def checkType(self, actualType, expectedTypeName):
        if actualType.name != expectedTypeName:
            raise Exception(f"expect {expectedTypeName}, but found {actualType.name}")
        return self.RValueCast(actualType)

    def RValueCast(self, actualType):
        if actualType.valueCat == ValueCat.Rvalue:
            return actualType
        else:
            self.pop("t0")
            self.asm.append(("# cast lvalue to rvalue\n"
                             "\tlw t0, 0(t0)\n"
                             ))
            self.push("t0")
            return actualType.valueCast(ValueCat.Rvalue)

    # 将寄存器的值压入栈中
    def push(self, reg: str):
        self.asm.extend(["# push " + reg + "\n", "\taddi sp, sp, -4\n", "\tsw " + reg + ", 0(sp)\n"])

    # 栈顶的值弹出到寄存器中
    def pop(self, reg: str):
        self.asm.extend(["# pop " + reg + "\n", "\tlw " + reg + ", 0(sp)\n", "\taddi sp, sp, 4\n"])

    # 从符号表寻找 优先从内层作用域中寻找
    def lookupSymbol(self, v: str):
        for i in range(len(self.symbolTable) - 1, -1, -1):
            map = self.symbolTable[i]
            if map.__contains__(v):
                return map.get(v)
        return None

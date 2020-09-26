from .generated.MiniDecafLexer import MiniDecafLexer
from .generated.MiniDecafParser import MiniDecafParser
from .generated.MiniDecafVisitor import MiniDecafVisitor
from .Type import *
from .utils import *

INT_MAX = 2147483647
INT_MIN = -2147483648


class MainVisitor(MiniDecafVisitor):
    def __init__(self):
        self.asm = ""
        self.containsMain = False

    def visitProg(self, ctx: MiniDecafParser.ProgContext):
        self.visit(ctx.func())
        if not self.containsMain:
            raise Exception("main function not found")

        return NoType()

    def visitFunc(self, ctx: MiniDecafParser.FuncContext):
        funcName = ctx.Ident().getText()
        if funcName == "main":
            self.containsMain = True
        self.asm += "".join(["\t.text\n", "\t.global " + funcName + "\n", funcName + ":\n"])
        self.visit(ctx.stmt())
        return NoType()

    def visitStmt(self, ctx: MiniDecafParser.StmtContext):
        self.visit(ctx.expr())
        self.asm += "# ret\n"
        self.pop("a0")
        self.asm += "\tret\n"
        return NoType()

    def visitExpr(self, ctx: MiniDecafParser.ExprContext):
        return self.visit(ctx.add())

    def visitAdd(self, ctx: MiniDecafParser.AddContext):
        if len(ctx.children) > 1:
            self.visit(ctx.add(0))
            self.visit(ctx.add(1))
            self.pop("t1")
            self.pop("t0")
            op = ctx.children[1].getText()
            self.asm += RulesToAsm[op]
            self.push("t0")
            return IntType()
        else:
            return self.visit(ctx.mul())

    def visitMul(self, ctx: MiniDecafParser.MulContext):
        if len(ctx.children) > 1:
            self.visit(ctx.mul(0))
            self.visit(ctx.mul(1))
            self.pop("t1")
            self.pop("t0")
            op = ctx.children[1].getText()
            self.asm += RulesToAsm[op]
            self.push("t0")
            return IntType()
        else:
            return self.visit(ctx.unary())

    def visitUnary(self, ctx: MiniDecafParser.UnaryContext):
        if len(ctx.children) > 1:
            self.visit(ctx.unary())
            op = ctx.children[0].getText()
            # 特判一下 - 因为与减符号相同无法使用字典
            self.pop("t0")
            if op == "-":
                self.asm += "# - int\n"
                self.asm += "\tneg t0, t0\n"
            else:
                self.asm += RulesToAsm[op]
            self.push("t0")
            return IntType()
        else:
            return self.visit(ctx.primary())

    def visitNumPrimary(self, ctx: MiniDecafParser.NumPrimaryContext):
        if int(ctx.Integer().getText()) > INT_MAX:
            raise Exception("large number")

        self.asm += "".join(["# number " + ctx.Integer().getText() + "\n",
                             "\tli t0, " + ctx.Integer().getText() + "\n"])
        self.push("t0")
        return IntType()

    def visitParenthesizedPrimary(self, ctx: MiniDecafParser.ParenthesizedPrimaryContext):
        return self.visit(ctx.expr())

    # 将寄存器的值压入栈中
    def push(self, reg: str):
        self.asm += "".join(["# push " + reg + "\n", "\taddi sp, sp, -4\n", "\tsw " + reg + ", 0(sp)\n"])

    # 栈顶的值弹出到寄存器中
    def pop(self, reg: str):
        self.asm += "".join(["# pop " + reg + "\n", "\tlw " + reg + ", 0(sp)\n", "\taddi sp, sp, 4\n"])

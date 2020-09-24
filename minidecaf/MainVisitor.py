from .generated.MiniDecafLexer import MiniDecafLexer
from .generated.MiniDecafParser import MiniDecafParser
from .generated.MiniDecafVisitor import MiniDecafVisitor
from .Type import *

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
        self.asm += "\tret\n"
        return NoType()

    def visitExpr(self, ctx: MiniDecafParser.ExprContext):
        numNode = ctx.Integer()
        numInt = int(numNode.getText())
        if numInt < 0 or numInt > INT_MAX:
            raise Exception("Int overflow")
        self.asm += "".join(["\t# number " + numNode.getText() + "\n", "\tli a0, " + numNode.getText() + "\n"])
        return IntType()

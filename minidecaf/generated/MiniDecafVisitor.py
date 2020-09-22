# Generated from MiniDecaf.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniDecafParser import MiniDecafParser
else:
    from MiniDecafParser import MiniDecafParser

# This class defines a complete generic visitor for a parse tree produced by MiniDecafParser.

class MiniDecafVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniDecafParser#prog.
    def visitProg(self, ctx:MiniDecafParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#func.
    def visitFunc(self, ctx:MiniDecafParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#ty.
    def visitTy(self, ctx:MiniDecafParser.TyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#stmt.
    def visitStmt(self, ctx:MiniDecafParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniDecafParser#expr.
    def visitExpr(self, ctx:MiniDecafParser.ExprContext):
        return self.visitChildren(ctx)



del MiniDecafParser
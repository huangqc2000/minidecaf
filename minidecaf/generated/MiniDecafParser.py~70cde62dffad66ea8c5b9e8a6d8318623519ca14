# Generated from MiniDecaf.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write("\'\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\5\3")
        buf.write("\5\3\5\3\5\3\6\3\6\3\7\3\7\3\7\5\7%\n\7\3\7\2\2\b\2\4")
        buf.write("\6\b\n\f\2\3\3\2\n\f\2!\2\16\3\2\2\2\4\21\3\2\2\2\6\31")
        buf.write("\3\2\2\2\b\33\3\2\2\2\n\37\3\2\2\2\f$\3\2\2\2\16\17\5")
        buf.write("\4\3\2\17\20\7\2\2\3\20\3\3\2\2\2\21\22\5\6\4\2\22\23")
        buf.write("\7\20\2\2\23\24\7\3\2\2\24\25\7\4\2\2\25\26\7\5\2\2\26")
        buf.write("\27\5\b\5\2\27\30\7\6\2\2\30\5\3\2\2\2\31\32\7\7\2\2\32")
        buf.write("\7\3\2\2\2\33\34\7\b\2\2\34\35\5\n\6\2\35\36\7\t\2\2\36")
        buf.write("\t\3\2\2\2\37 \5\f\7\2 \13\3\2\2\2!\"\t\2\2\2\"%\5\f\7")
        buf.write("\2#%\7\21\2\2$!\3\2\2\2$#\3\2\2\2%\r\3\2\2\2\3$")
        return buf.getvalue()


class MiniDecafParser ( Parser ):

    grammarFileName = "MiniDecaf.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "'int'", "'return'", 
                     "';'", "'-'", "'!'", "'~'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "WS", "COMMENT", 
                      "LINE_COMMENT", "IDENT", "NUM" ]

    RULE_prog = 0
    RULE_func = 1
    RULE_ty = 2
    RULE_stmt = 3
    RULE_expr = 4
    RULE_unary = 5

    ruleNames =  [ "prog", "func", "ty", "stmt", "expr", "unary" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    WS=11
    COMMENT=12
    LINE_COMMENT=13
    IDENT=14
    NUM=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func(self):
            return self.getTypedRuleContext(MiniDecafParser.FuncContext,0)


        def EOF(self):
            return self.getToken(MiniDecafParser.EOF, 0)

        def getRuleIndex(self):
            return MiniDecafParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = MiniDecafParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.func()
            self.state = 13
            self.match(MiniDecafParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ty(self):
            return self.getTypedRuleContext(MiniDecafParser.TyContext,0)


        def IDENT(self):
            return self.getToken(MiniDecafParser.IDENT, 0)

        def stmt(self):
            return self.getTypedRuleContext(MiniDecafParser.StmtContext,0)


        def getRuleIndex(self):
            return MiniDecafParser.RULE_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc" ):
                listener.enterFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc" ):
                listener.exitFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc" ):
                return visitor.visitFunc(self)
            else:
                return visitor.visitChildren(self)




    def func(self):

        localctx = MiniDecafParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.ty()
            self.state = 16
            self.match(MiniDecafParser.IDENT)
            self.state = 17
            self.match(MiniDecafParser.T__0)
            self.state = 18
            self.match(MiniDecafParser.T__1)
            self.state = 19
            self.match(MiniDecafParser.T__2)
            self.state = 20
            self.stmt()
            self.state = 21
            self.match(MiniDecafParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniDecafParser.RULE_ty

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTy" ):
                listener.enterTy(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTy" ):
                listener.exitTy(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTy" ):
                return visitor.visitTy(self)
            else:
                return visitor.visitChildren(self)




    def ty(self):

        localctx = MiniDecafParser.TyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_ty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(MiniDecafParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniDecafParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniDecafParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MiniDecafParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(MiniDecafParser.T__5)
            self.state = 26
            self.expr()
            self.state = 27
            self.match(MiniDecafParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary(self):
            return self.getTypedRuleContext(MiniDecafParser.UnaryContext,0)


        def getRuleIndex(self):
            return MiniDecafParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MiniDecafParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.unary()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary(self):
            return self.getTypedRuleContext(MiniDecafParser.UnaryContext,0)


        def NUM(self):
            return self.getToken(MiniDecafParser.NUM, 0)

        def getRuleIndex(self):
            return MiniDecafParser.RULE_unary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary" ):
                listener.enterUnary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary" ):
                listener.exitUnary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary" ):
                return visitor.visitUnary(self)
            else:
                return visitor.visitChildren(self)




    def unary(self):

        localctx = MiniDecafParser.UnaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_unary)
        self._la = 0 # Token type
        try:
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniDecafParser.T__7, MiniDecafParser.T__8, MiniDecafParser.T__9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniDecafParser.T__7) | (1 << MiniDecafParser.T__8) | (1 << MiniDecafParser.T__9))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 32
                self.unary()
                pass
            elif token in [MiniDecafParser.NUM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.match(MiniDecafParser.NUM)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






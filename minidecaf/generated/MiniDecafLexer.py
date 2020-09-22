# Generated from MiniDecaf.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16")
        buf.write("Y\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n")
        buf.write("\3\n\7\n9\n\n\f\n\16\n<\13\n\3\n\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\7\13G\n\13\f\13\16\13J\13\13\3\13\3\13")
        buf.write("\3\f\3\f\7\fP\n\f\f\f\16\fS\13\f\3\r\6\rV\n\r\r\r\16\r")
        buf.write("W\3:\2\16\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\3\2\7\5\2\13\f\16\17\"\"\4\2\f\f\17\17\5")
        buf.write("\2C\\aac|\6\2\62;C\\aac|\3\2\62;\2\\\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\3\33\3\2\2\2\5\35\3\2\2\2\7")
        buf.write("\37\3\2\2\2\t!\3\2\2\2\13#\3\2\2\2\r\'\3\2\2\2\17.\3\2")
        buf.write("\2\2\21\60\3\2\2\2\23\64\3\2\2\2\25B\3\2\2\2\27M\3\2\2")
        buf.write("\2\31U\3\2\2\2\33\34\7*\2\2\34\4\3\2\2\2\35\36\7+\2\2")
        buf.write("\36\6\3\2\2\2\37 \7}\2\2 \b\3\2\2\2!\"\7\177\2\2\"\n\3")
        buf.write("\2\2\2#$\7k\2\2$%\7p\2\2%&\7v\2\2&\f\3\2\2\2\'(\7t\2\2")
        buf.write("()\7g\2\2)*\7v\2\2*+\7w\2\2+,\7t\2\2,-\7p\2\2-\16\3\2")
        buf.write("\2\2./\7=\2\2/\20\3\2\2\2\60\61\t\2\2\2\61\62\3\2\2\2")
        buf.write("\62\63\b\t\2\2\63\22\3\2\2\2\64\65\7\61\2\2\65\66\7,\2")
        buf.write("\2\66:\3\2\2\2\679\13\2\2\28\67\3\2\2\29<\3\2\2\2:;\3")
        buf.write("\2\2\2:8\3\2\2\2;=\3\2\2\2<:\3\2\2\2=>\7,\2\2>?\7\61\2")
        buf.write("\2?@\3\2\2\2@A\b\n\2\2A\24\3\2\2\2BC\7\61\2\2CD\7\61\2")
        buf.write("\2DH\3\2\2\2EG\n\3\2\2FE\3\2\2\2GJ\3\2\2\2HF\3\2\2\2H")
        buf.write("I\3\2\2\2IK\3\2\2\2JH\3\2\2\2KL\b\13\2\2L\26\3\2\2\2M")
        buf.write("Q\t\4\2\2NP\t\5\2\2ON\3\2\2\2PS\3\2\2\2QO\3\2\2\2QR\3")
        buf.write("\2\2\2R\30\3\2\2\2SQ\3\2\2\2TV\t\6\2\2UT\3\2\2\2VW\3\2")
        buf.write("\2\2WU\3\2\2\2WX\3\2\2\2X\32\3\2\2\2\7\2:HQW\3\b\2\2")
        return buf.getvalue()


class MiniDecafLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    WS = 8
    COMMENT = 9
    LINE_COMMENT = 10
    IDENT = 11
    NUM = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'{'", "'}'", "'int'", "'return'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "COMMENT", "LINE_COMMENT", "IDENT", "NUM" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "WS", "COMMENT", "LINE_COMMENT", "IDENT", "NUM" ]

    grammarFileName = "MiniDecaf.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



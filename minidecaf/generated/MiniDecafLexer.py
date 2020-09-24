# Generated from MiniDecaf.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16")
        buf.write("e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\3\3\3\3\4\3\4\3\5")
        buf.write("\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\7\n?\n\n\f\n\16\nB")
        buf.write("\13\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\7\13M\n")
        buf.write("\13\f\13\16\13P\13\13\3\13\3\13\3\f\3\f\7\fV\n\f\f\f\16")
        buf.write("\fY\13\f\3\r\6\r\\\n\r\r\r\16\r]\3\16\3\16\3\17\3\17\3")
        buf.write("\20\3\20\3@\2\21\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\2\35\2\37\2\3\2\7\5\2\13\f\16\17")
        buf.write("\"\"\4\2\f\f\17\17\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\2")
        buf.write("e\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\3!\3\2\2")
        buf.write("\2\5#\3\2\2\2\7%\3\2\2\2\t\'\3\2\2\2\13)\3\2\2\2\r-\3")
        buf.write("\2\2\2\17\64\3\2\2\2\21\66\3\2\2\2\23:\3\2\2\2\25H\3\2")
        buf.write("\2\2\27S\3\2\2\2\31[\3\2\2\2\33_\3\2\2\2\35a\3\2\2\2\37")
        buf.write("c\3\2\2\2!\"\7*\2\2\"\4\3\2\2\2#$\7+\2\2$\6\3\2\2\2%&")
        buf.write("\7}\2\2&\b\3\2\2\2\'(\7\177\2\2(\n\3\2\2\2)*\7k\2\2*+")
        buf.write("\7p\2\2+,\7v\2\2,\f\3\2\2\2-.\7t\2\2./\7g\2\2/\60\7v\2")
        buf.write("\2\60\61\7w\2\2\61\62\7t\2\2\62\63\7p\2\2\63\16\3\2\2")
        buf.write("\2\64\65\7=\2\2\65\20\3\2\2\2\66\67\t\2\2\2\678\3\2\2")
        buf.write("\289\b\t\2\29\22\3\2\2\2:;\7\61\2\2;<\7,\2\2<@\3\2\2\2")
        buf.write("=?\13\2\2\2>=\3\2\2\2?B\3\2\2\2@A\3\2\2\2@>\3\2\2\2AC")
        buf.write("\3\2\2\2B@\3\2\2\2CD\7,\2\2DE\7\61\2\2EF\3\2\2\2FG\b\n")
        buf.write("\2\2G\24\3\2\2\2HI\7\61\2\2IJ\7\61\2\2JN\3\2\2\2KM\n\3")
        buf.write("\2\2LK\3\2\2\2MP\3\2\2\2NL\3\2\2\2NO\3\2\2\2OQ\3\2\2\2")
        buf.write("PN\3\2\2\2QR\b\13\2\2R\26\3\2\2\2SW\5\33\16\2TV\5\35\17")
        buf.write("\2UT\3\2\2\2VY\3\2\2\2WU\3\2\2\2WX\3\2\2\2X\30\3\2\2\2")
        buf.write("YW\3\2\2\2Z\\\5\37\20\2[Z\3\2\2\2\\]\3\2\2\2][\3\2\2\2")
        buf.write("]^\3\2\2\2^\32\3\2\2\2_`\t\4\2\2`\34\3\2\2\2ab\t\5\2\2")
        buf.write("b\36\3\2\2\2cd\t\6\2\2d \3\2\2\2\7\2@NW]\3\b\2\2")
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
    Whitespace = 8
    COMMENT = 9
    LINE_COMMENT = 10
    Ident = 11
    Integer = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'{'", "'}'", "'int'", "'return'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "Whitespace", "COMMENT", "LINE_COMMENT", "Ident", "Integer" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "Whitespace", "COMMENT", "LINE_COMMENT", "Ident", "Integer", 
                  "IdentLead", "WordChar", "Digit" ]

    grammarFileName = "MiniDecaf.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



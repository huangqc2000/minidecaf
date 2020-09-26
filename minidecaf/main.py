from minidecaf.MainVisitor import MainVisitor
import sys
import argparse
from antlr4 import *

from .generated.MiniDecafLexer import MiniDecafLexer
from .generated.MiniDecafParser import MiniDecafParser


def parseArgs(argv):
    parser = argparse.ArgumentParser(description="MiniDecaf compiler")
    parser.add_argument("inputfile", type=str,
                        help="the input C file")
    parser.add_argument("outputfile", type=str, nargs="?",
                        help="the output assembly file")
    return parser.parse_args()


def main():
    args = parseArgs(sys.argv)
    inputStream = FileStream(args.inputfile)
    lexer = MiniDecafLexer(inputStream)
    # dumpLexerTokens(lexer)
    tokenStream = CommonTokenStream(lexer)
    parser = MiniDecafParser(tokenStream)
    parser._errHandler = BailErrorStrategy()
    tree = parser.prog()
    visitor = MainVisitor()
    visitor.visit(tree)
    asm = visitor.asm
    print(asm)
    # with open(args.outputfile, 'w') as fout:
    #     fout.write(asm)

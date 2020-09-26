RulesToAsm = {"+": "# int + int\n\tadd t0, t0, t1\n",
              "-": "# int - int\n\tsub t0, t0, t1\n",
              "*": "# *\n\tmul t0, t0, t1\n",
              "/": "# /\n\tdiv t0, t0, t1\n",
              "%": "# %\n\trem t0, t0, t1\n",
              "!": "# ! int\n\tseqz t0, t0\n",
              "~": "# ~ int\n\tnot t0, t0\n",
              "||": "# int || int\tsnez t0, t0\n\tsnez t1, t1\n\tor t0, t0, t1\n",
              "&&": "# int && int\tsnez t0, t0\n\tsnez t1, t1\n\tand t0, t0, t1\n",
              "==": "# equal\n\tsub t0, t0, t1\n\tseqz t0, t0\n",
              "!=": "# not equal\n\tsub t0, t0, t1\n\tsnez t0, t0\n",
              "<": "# <\n\tslt t0, t0, t1\n",
              "<=": "# <=\n\tsgt t0, t0, t1\n\txori t0, t0, 1\n",
              ">": "# >\n\tsgt t0, t0, t1\n",
              ">=": "# >=\n\tslt t0, t0, t1\n\txori t0, t0, 1\n",
              }


def getSymbolicNames(Lexer: type):
    intAttrs = set([a for a in dir(Lexer) if type(getattr(Lexer, a)) is int])
    ignoreAttrs = {"DEFAULT_MODE", "DEFAULT_TOKEN_CHANNEL", "HIDDEN",
                   "MAX_CHAR_VALUE", "MIN_CHAR_VALUE", "MORE", "SKIP"}
    symNames = intAttrs - ignoreAttrs
    return {getattr(Lexer, a): a for a in symNames}


def dumpLexerTokens(lexer):
    symNames = getSymbolicNames(type(lexer))
    print(f"{'Token':<10} {'Text':<20}")
    print(f"{'-' * 9:<10} {'-' * 19:<20}")
    for token in lexer.getAllTokens():
        symName = symNames[token.type]
        print(f"{symName:<10} {token.text:<40}")

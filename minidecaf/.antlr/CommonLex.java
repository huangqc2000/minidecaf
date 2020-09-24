// Generated from /mnt/e/大三上/编译原理/minidecaf-hqc/minidecaf/minidecaf/CommonLex.g4 by ANTLR 4.8
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class CommonLex extends Lexer {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		Integer=1, Whitespace=2, Ident=3;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"Integer", "Whitespace", "Ident", "IdentLead", "WordChar", "Digit"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "Integer", "Whitespace", "Ident"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public CommonLex(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "CommonLex.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\5(\b\1\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2\6\2\21\n\2\r\2\16\2\22\3\3"+
		"\6\3\26\n\3\r\3\16\3\27\3\3\3\3\3\4\3\4\7\4\36\n\4\f\4\16\4!\13\4\3\5"+
		"\3\5\3\6\3\6\3\7\3\7\2\2\b\3\3\5\4\7\5\t\2\13\2\r\2\3\2\6\5\2\13\f\17"+
		"\17\"\"\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\2\'\2\3\3\2\2\2\2\5\3\2\2\2"+
		"\2\7\3\2\2\2\3\20\3\2\2\2\5\25\3\2\2\2\7\33\3\2\2\2\t\"\3\2\2\2\13$\3"+
		"\2\2\2\r&\3\2\2\2\17\21\5\r\7\2\20\17\3\2\2\2\21\22\3\2\2\2\22\20\3\2"+
		"\2\2\22\23\3\2\2\2\23\4\3\2\2\2\24\26\t\2\2\2\25\24\3\2\2\2\26\27\3\2"+
		"\2\2\27\25\3\2\2\2\27\30\3\2\2\2\30\31\3\2\2\2\31\32\b\3\2\2\32\6\3\2"+
		"\2\2\33\37\5\t\5\2\34\36\5\13\6\2\35\34\3\2\2\2\36!\3\2\2\2\37\35\3\2"+
		"\2\2\37 \3\2\2\2 \b\3\2\2\2!\37\3\2\2\2\"#\t\3\2\2#\n\3\2\2\2$%\t\4\2"+
		"\2%\f\3\2\2\2&\'\t\5\2\2\'\16\3\2\2\2\6\2\22\27\37\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
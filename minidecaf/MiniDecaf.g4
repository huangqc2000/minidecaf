grammar MiniDecaf;

prog:
	(func | globalDecl)* EOF;

func:
	ty Ident '(' (ty Ident (',' ty Ident)*)? ')' '{' blockItem* '}'	# definedFunc
	| ty Ident '(' (ty Ident (',' ty Ident)*)? ')' ';'				# declaredFunc;

ty: 'int' '*'*;

blockItem: localDecl | stmt;

globalDecl:
	ty Ident ('=' Integer)? ';'		# globalIntOrPointerDecl
	| ty Ident ('[' Integer ']')+ ';'	# globalArrayDecl
	;

localDecl:
	ty Ident ('=' expr)? ';'		# localIntOrPointerDecl
	| ty Ident ('[' Integer ']')+ ';'	# localArrayDecl
	;

stmt:
	expr? ';' # exprStmt
	| 'return' expr ';' # returnStmt
	| 'if' '(' expr ')' stmt ('else' stmt)? # ifStmt
	| '{' blockItem* '}' # blockStmt
	| 'while' '(' expr ')' stmt # whileStmt
	| 'for' '(' (localDecl | expr? ';') expr? ';' expr? ')' stmt	# forStmt
	| 'do' stmt 'while' '(' expr ')' ';' # doStmt
	| 'break' ';' # breakStmt
	| 'continue' ';' # continueStmt
	;

expr: unary '=' expr | ternary;

ternary: lor '?' expr ':' ternary | lor;

lor: lor '||' lor | land;

land: land '&&' land | equ;

equ: equ ('==' | '!=') equ | rel;

rel: rel ('<'|'>'|'<='|'>=') rel | add;

add: add ('+' | '-') add | mul;

mul: mul ('*' | '/' | '%') mul | unary;

unary:
	('-' | '~' | '!' | '&' | '*') unary	# opUnary
	| '(' ty ')' unary # castUnary
	| postfix # postfixUnary;

postfix:
	Ident '(' (expr (',' expr)*)? ')' # callPostfix
	| postfix '[' expr ']' # subscriptPostfix
	| primary # primaryPostfix
	;


primary:
	Integer # numPrimary
	| Ident # IdentPrimary
	| '(' expr ')' # parenthesizedPrimary
	;


/* lexer */
Whitespace: [ \t\r\n\u000C] -> skip;

// comment
// The specification of minidecaf doesn't allow commenting,
// but we provide the comment feature here for the convenience of debugging.
COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;

Ident: IdentLead WordChar*;
Integer: Digit+;
fragment IdentLead: [a-zA-Z_];
fragment WordChar: [0-9a-zA-Z_];
fragment Digit: [0-9];
grammar MiniDecaf;

prog:
	func EOF;

func: ty Ident '(' ')' '{' blockItem* '}';

ty: 'int';

blockItem: localDecl | stmt;

localDecl: ty Ident ('=' expr)? ';';

stmt:
	expr? ';' # exprStmt
	| 'return' expr ';' # returnStmt
	| 'if' '(' expr ')' stmt ('else' stmt)? # ifStmt
	| '{' blockItem* '}' # blockStmt
	;

expr: Ident '=' expr | ternary;

ternary: lor '?' expr ':' ternary | lor;

lor: lor '||' lor | land;

land: land '&&' land | equ;

equ: equ ('==' | '!=') equ | rel;

rel: rel ('<'|'>'|'<='|'>=') rel | add;

add: add ('+' | '-') add | mul;

mul: mul ('*' | '/' | '%') mul | unary;

unary: ('-' | '!' | '~') unary | primary;

primary:
	Integer # numPrimary
	| Ident # identPrimary
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
grammar MiniDecaf;

prog:
	func EOF;

func: ty Ident '(' ')' '{' stmt '}';

ty: 'int';

stmt: 'return' expr ';';

expr: unary;

unary: ('-' | '!' | '~') unary | Integer;

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


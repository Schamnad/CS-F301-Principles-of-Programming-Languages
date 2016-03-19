COMMAND LINE RUN STATEMENT: python src/main.py testcases/test2.txt error.txt tokens.txt category.txt

Deliverables:
a) error.txt
	Detects Lexical errors
	Format [(lineNo; Postion);Token that violates thhe lexical rules]

b) tokens.txt
	Classifies each Lexeme into different tokens
	Provides output in the format [Token type; Token Value; Line Number; Position]

c)category.txt
	Provides output which matches each token to its Category.
	Format [Category:- Token]


Status of the code:
Working
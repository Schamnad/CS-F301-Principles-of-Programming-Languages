# CS-F301-Principles-of-Programming-Languages
Principles of Programming Languages course completed at BITS-Pilani, Pilani Campus in the first semester of 2014

Designed a Domain Specific Programming language aimed at the Automotive industry. Implemented a Lexer for this programming language.

Read Language-Design.docx and Language-Details.docx for more details about the project

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

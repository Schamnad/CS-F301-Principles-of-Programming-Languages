import sys
import LexicalAnalyzer
from LEXER_DATA import regexes

#COMMAND LINE RUN STATEMENT: python src/main.py testcases/test2.txt error.txt tokens.txt category.txt
   
codeFileName    =  sys.argv[1]       
errorFileName   =  sys.argv[2]
tokFileName     =  sys.argv[3]
catFileName 	=  sys.argv[4]
					
lerror = 0
LexicalAnalyzer.controlLexer(tokFileName,errorFileName,codeFileName,catFileName,lerror) 

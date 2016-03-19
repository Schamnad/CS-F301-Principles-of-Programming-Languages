import re
import sys
from LEXER_DATA import regexes

def controlLexer(tokfilename,errorfilename,codefilename,catFile,lerror):
	codeFile  = open(codefilename,"r")       
	errorFile = open(errorfilename,"w")
	tokFile   = open(tokfilename,"w+")
	categoryFile = open(catFile,"w+")
	lx = Lexer(regexes)
	
	lineNo = 1
	
	for line in codeFile:
		lx.input(line,lineNo)
		tokensAll = lx.allTokens()
		
		for tok in tokensAll:
			if tok.type == 'ToK_ERROR':
				print("Program has lexical errors. Check the error file")
				errorFile.write('LineNo: %d,  Token Position: %d  \'%s\' doesn\'t follow the lexical rules \n' %(lineNo,tok.pos,tok.val))
				lerror = 1
			elif tok.type == 'TK_CMNT':
				continue
			else:
				tokFile.write(str(tok))
				categoryFile.write(tok.category()) 
				
		lineNo = lineNo + 1
		
	tokFile.close()
	categoryFile.close()
	if lerror:
		exit()
		
		
class Lexeme(): #Defines the identified lexeme with its value, position and token type
			
	def __init__(self, type, value, pos, lineNo): #default initialization constructor
		self.lineNo = lineNo
		self.val = value
		self.pos = pos
		self.type = type
		
	def __str__(self):		
		return '%s %s %s %s \n' %(self.type, self.val, self.lineNo, self.pos)
	
	#used to print out the tokens category wise
	def category(self):
		if self.val in '+-*/%=' :
			return 'Operator:-%s \n' %(self.val.rjust(22))
		elif self.type in ['TK_FUNC_IDTFR','TK_IDTFR']: 
			return 'Identifier:-\t\t%s \n' %(self.val.rjust(14))
		elif self.val in '().:$#;,' :
			return 'Special symbol:-\t\t%s \n' %(self.val.rjust(10))
		elif self.type in ['TK_CONST_RLNUM','TK_CONST_NUM','TK_CONST_STRING','TK_CONST_TIME']:
			return 'Constant:-\t\t%s \n' %(self.val.rjust(18))
		else:
			return 'Keyword:-\t\t%s \n' %(self.val.rjust(18))
	
		
class Lexer():
	#The main work happens here. Lexer class
	
	def __init__(self, regexes):
		#The entire process uses the regular expressions frequently. 
		#Hence it is much more efficient to collect all the definitions in one place, in a section of code that compiles all the REs ahead of time.
		#Named groups are created for each type of R.E
		
		count = 1
		self.group_type = {}
		partRegex = []
			
		self.re_whiteSpace = re.compile('\s|\n') 		#a regex to find white spaces
		self.re_skipWhiteSpace = re.compile('\S')  		#regex which detects a string without white spaces
		
		for regex, type in regexes:
			groupName = 'GROUP%s' % count
			partRegex.append('(?P<%s>%s)' %(groupName,regex))  #makes a list with a a pair consisting of the groupname and the corresponding R.E
			self.group_type[groupName] = type
			count = count + 1
				
		self.regex = re.compile('|'.join(partRegex))   #all regexes are compiled to one single object which makes further operations on regexes efficient
		
	
	def input(self, buff, buffLine):  #initialization of the input buffer 
		self.pos = 0
		self.buff = buff
		self.lineNo = buffLine
				
	def token(self):
		# Returns the next lexeme as an object(Lexeme object) from the input buffer
		# checks if the end of the buffer is reached
		# When a token is not recognized, the starting position of that token is recorded for the lexical errorfile
		
		if self.pos >= len(self.buff):
			return None
		else:
			nextUnit = self.re_skipWhiteSpace.search(self.buff, self.pos)  #returns a group of characters without white spaces
			
		if nextUnit:
			self.pos = nextUnit.start()
		else:
			return None
				
		nextUnit = self.regex.match(self.buff,self.pos) 					#finds whether the Unit selected is a part of the Lexeme
			
		if nextUnit:
			groupName = nextUnit.lastgroup
			tokType = self.group_type[groupName]
			tokn = Lexeme(tokType, nextUnit.group(groupName),self.pos, self.lineNo)
			self.pos = nextUnit.end()
			return tokn
				
		#if the token doesn't match any regex
		whiteSpaceMatch = self.re_whiteSpace.search(self.buff, self.pos)
		start = self.pos
		end = whiteSpaceMatch.start()
		tokn = Lexeme('ToK_ERROR', self.buff[start:end],start,self.lineNo)
		self.pos = whiteSpaceMatch.end()
		return tokn
		
	def allTokens(self): 													# Returns an iterator to the tokens found in the buffer.
		tokensPerLine = []
		tokn = self.token()
		
		while(tokn):
			tokensPerLine.append(tokn)
			tokn = self.token()
			
		return tokensPerLine
		
		
				
				
				
			
YACC_FILE = ./src/parser.y
LEX_FILE = ./src/parser.l

YACC_FILE_HEADER = ./include/y.tab.h

YACC_FILE_COMPILED = ./src/y.tab.c
LEX_FILE_COMPILED = ./src/lex.yy.c

PARSER = ./bin/parser

INCLUDE_FILES = ./include/*.h



all : build

build :
	# compiling yacc files
	yacc -d $(YACC_FILE)
	mv y.tab.h $(YACC_FILE_HEADER) | true
	mv y.tab.c $(YACC_FILE_COMPILED) | true
	# compiling lex files
	lex $(LEX_FILE)
	mv lex.yy.c $(LEX_FILE_COMPILED) | true
	# compiling src files
	g++ $(YACC_FILE_COMPILED) $(LEX_FILE_COMPILED) -o $(PARSER)

run : 
	./bin/compiler
	

clean :
	# removing y.tab.c and y.tab.h
	rm $(YACC_FILE_HEADER) $(YACC_FILE_COMPILED) | true
	# removing lex.yy.c
	rm $(LEX_FILE_COMPILED) | true
	# removing executable
	rm $(PARSER)
	
test : build run clean








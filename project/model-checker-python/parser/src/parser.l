%{
	#include<stdio.h>
	#include<stdlib.h>
	#include<string.h>
	#include "../include/y.tab.h"
%}

propositional_variables [a-z]

%%
[ \t]		{}

{propositional_variables}	{ printf("%s\n", yytext); }

EF	{ printf("%s\n", yytext); return EF;}

EG	{ printf("%s\n", yytext); return EG;}

AF	{ printf("%s\n", yytext); return AF;}

AG	{ printf("%s\n", yytext); return AG;}

EX	{ return EX; }

AX	{ return AX; }

A	{ return A; }

E	{ return E; }

U	{ return U; }

T	{ return TRUE; }

F	{ return FALSE; }

\[\]	{ printf("%s", yytext); }

\n	{}

%%

int yywrap(){
	return 1;
}














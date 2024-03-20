%{
	#include<stdio.h>
	// #include "y.tab.h"
%}

propositional_variables [a-z]

%%
[ \t]		{}

{propositional_variables}	{ printf("%s\n", yytext); }

EF	{ printf("%s\n", yytext); }

EG	{ printf("%s\n", yytext); }

AF	{ printf("%s\n", yytext); }

AG	{ printf("%s\n", yytext); }

\[\]	{ printf("%s", yytext);}

\n	{}

%%

int yywrap(){
	return 1;
}

int main(){
	yylex();
}













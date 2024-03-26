%{
#include <stdio.h>
#include <stdlib.h>
#include<string.h>
%}

%token PROP_VARIABLE
%token L_PARENTHESES R_PARENTHESES
%token NOT
%token AND OR IMPLIES
%token EF EG AF AG EX AX
%token L_SQUARE R_SQUARE
%token EU AU
%token E A U
%token TRUE FALSE

%left OR AND
%right IMPLIES
%right NOT

%%

formula : TRUE 
		| FALSE
		| PROP_VARIABLE
		| or_formula
		| and_formula
		| implication_formula
		| not_formula
		| x_formula
		| f_formula
		| g_formula
		| u_formula
		;

or_formula : formula OR formula
		   ;

and_formula : formula AND formula
			;

implication_formula : formula IMPLIES formula
					;

not_formula : NOT formula
			;

x_formula : EX '(' formula ')'
		  | AX '(' formula ')'
		  ;

f_formula : EF '(' formula ')'
		  | AF '(' formula ')'
		  ;

g_formula : EG '(' formula ')'
		  | AG '(' formula ')'
		  ;

u_formula : E '[' formula 'U' ']'
		  | A '[' formula 'U' ']'
		  ;

%%

int yyerror(char *s){
	
}

int main(){
	yyparse();
	return 0;
}






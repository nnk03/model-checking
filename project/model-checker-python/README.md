# CTL Model Checker in Python

This is a CTL model checker using the model checking algorithms
implemented using Python3

In order to use this you need to have `ply` installed which is a package for
python for implementing the parser using lex and yacc for python. The following is the link to
the package [https://pypi.org/project/ply/](PLY)

Run the below command, preferably in a virtual environment

```
pip install -r requirements.txt
```

or extract the zip file and go to the folder containing all the python files and run the following
commands

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

To deactivate the environment, run the below command

```
deactivate
```

```
Important assumption in this project

Input is assumed to be a valid Kripke structure, i.e every state has outgoing transitions. Didn't add
trap state because if trap state is added, then the labels to be assigned to the trap state would be ambigous.
```

[requirements.txt](./requirements.txt) is the file containing the required libraries of
this project

Steps done

```
1.  : Convert the formula ϕ into an equivalent formula ψ in which a
        conveninent minimal set of CTL operators only are used.

        1. Output the resultant formula ψ (mention which is the minimal set that you are choosing).
        2. Output the number of nodes (including leaves) in the parse tree of ψ.
        3. In the bottom-up order, for each node of the parse-tree,
            output the node-id and subformula corresponding to that node.
        4. Store the parse tree of ψ for later processing.

2.  : Implement the bottom-up CTL model checking algorithm that outputs the
        subset of states of K that satisfies ψ.
    Choose an appropriate data structure so that looking up the set of
        states that satisfy the formula(s) corresponding to the immediate subtrees of
    a node in the parse tree can be quickly done and
        the additional computation at a node is also efficiently done.
    Make sure that the time spent per node of the parse
        tree is at most quadratic (preferably linear) in the size of K.
    After processing each parse-tree node, output its node-id
        and the subset of states of K that satisfy the subformula corresponding to that node.
```

# Run the project

If input is in a file, then run [main.py](./main.py)
else run [main2.py](./main2.py)

The format of the testcase is mentioned last

## Syntax followed

```
formula : formula first_order_operator formula
        | '!' formula
        | '(' formula ')'
        | unary_temporal_operator formula
        | binary_temporal_formula
        | prop_variable
        | boolean
        ;

first_order_operator : '&'
                    |  '|'
                    |  '->'
                    ;

binary_temporal_formula : 'E' '[' formula 'U' formula ']'
                        | 'A' '[' formula 'U' formula ']'
                        ;

unary_temporal_operator : 'AG'
                        | 'EG'
                        | 'AF'
                        | 'EF'
                        | 'AX'
                        | 'EX'
                        ;


prop_variable : [a-z_][a-zA-Z_]*
                ;

boolean : 'T'
        | 'F'
        ;

```

## Precedence

Topmost operator is least precedence and
bottom most operator has the highest precedence

```
precedence = (
    ('left', '|'),
    ('left', '&'),
    ('right', '!'),
    ('right', '->'),
    ('right', 'EX'),
    ('right', 'AX'),
    ('right', 'EF'),
    ('right', 'AF'),
    ('right', 'EG'),
    ('right', 'AG'),
    ('left', 'EU'),
    ('right', 'AU')
)
```

## Test Case format

< Number of states of Kripke structure>\
< Number of propositional variables >\
< Names of the propositional variables
delimited by space
(
can be multicharactered, but should of the format `[a-z_][a-zA-Z_]*`
)>\
< Start states delimited by space (states are numbered from 0)>\
< Next states of 0 >\
< Next states of 1 >\
.\
.\
< Next states of $n - 1$ >\
< Labels for state 0 delimited by space >\
< Labels for state 1 delimited by space >\
.\
.\
< Labels for state $n - 1$ delimited by space >\
< CTL Formula 1 to be model checked >\
< CTL Formula 2 to be model checked >\
.\
.\
.\
< Till EOF >

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

[./requirements.txt](requirements.txt) is the file containing the required libraries of
this project

Steps done

```
1.  : Convert the formula ϕ into an equivalent formula ψ in which a conveninent minimal set of CTL operators only are used.

        1. Output the resultant formula ψ (mention which is the minimal set that you are choosing).
        2. Output the number of nodes (including leaves) in the parse tree of ψ.
        3. In the bottom-up order, for each node of the parse-tree, output the node-id and subformula corresponding to that node.
        4. Store the parse tree of ψ for later processing.

2.  : Implement the bottom-up CTL model checking algorithm that outputs the subset of states of K that satisfies ψ.
    Choose an appropriate data structure so that looking up the set of states that satisfy the formula(s) corresponding to the immediate subtrees of
    a node in the parse tree can be quickly done and the additional computation at a node is also efficiently done.
    Make sure that the time spent per node of the parse tree is at most quadratic (preferably linear) in the size of K.
    After processing each parse-tree node, output its node-id and the subset of states of K that satisfy the subformula corresponding to that node.
```

To see the project in action, run [./main.py](main.py)

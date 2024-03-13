# Input received as fully parenthesized CTL sub_formula
"""
Propositions are numbered
Negation is represented as '-'
"""

class Node():
    def __init__(self, 
                 value : str, 
                 isOperand : bool = False, 
                 isOperator : bool = True, 
                 isUnary : bool = False,
                 left = None,
                 right = None
                 ):
        self.value = value
        self.isOperand = isOperand
        self.isOperator = isOperator
        self.isUnary = isUnary
        self.left = left
        self.right = right
        self.sub_formula = ''
        sub_formula = ''
        if self.left != None:
            assert(isinstance(self.left, Node))
            sub_formula += self.left.sub_formula
        
        sub_formula += value

        if self.right != None:
            assert(isinstance(self.right, Node))
            sub_formula += self.right.sub_formula

        self.sub_formula = sub_formula




















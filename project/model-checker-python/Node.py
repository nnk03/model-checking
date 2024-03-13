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
                 right = None,
                 down = None
                 ):
        self.value = value
        self.isOperand = isOperand
        self.isOperator = isOperator
        self.isUnary = isUnary
        # left and right are for binary operators
        self.left = left
        self.right = right

        # down is for unary operators
        self.down = down

        # denotes the sub formula that this node represents
        self.sub_formula = ''

        sub_formula = ''
        if self.down != None:
            sub_formula += value
            assert(isinstance(self.down, Node))
            sub_formula += self.down.sub_formula
        else:
            if self.left != None:
                assert(isinstance(self.left, Node))
                sub_formula += self.left.sub_formula
            
            sub_formula += value

            if self.right != None:
                assert(isinstance(self.right, Node))
                sub_formula += self.right.sub_formula

        self.sub_formula = sub_formula

    def isLeaf(self):
        return self.left == None and self.right == None and self.down == None




















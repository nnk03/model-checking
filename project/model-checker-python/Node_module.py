# Input received as fully parenthesized CTL sub_formula
"""
Propositions are numbered
Negation is represented as '-'
"""

from globals import *
from State_module import State
from Proposition_module import Proposition

class Node():
    def __init__(self, 
                  # value : str, 
                 isOperand : bool = False, 
                 isOperator : bool = True, 
                 isUnary : bool = False,
                 isBool : bool = False,
                 left = None,
                 right = None,
                 down = None,
                 sub_tree_formula = None,
                 ):
        # self.value = value
        self.isBool = isBool
        self.isOperand = isOperand
        self.isOperator = isOperator
        self.isUnary = isUnary
        # left and right are for binary operators
        self.left = left
        self.right = right
        self.sub_tree_formula = sub_tree_formula

        # down is for unary operators
        self.down = down
        self.minimal_formula = ''

    def set_minimal_formula(self, formula = ''):
        result = ''
        if formula == '':
            if self.down != None and isinstance(self.down, Node):
                down_formula = str(self.down.minimal_formula)
                result = '(' + self.operator + ' '
                result += down_formula
                result += ')'

            elif self.left != None and self.right != None and isinstance(self.left, Node) and isinstance(self.right, Node):
                if self.operator == 'EU' or self.operator == 'AU':
                    left_formula = str(self.left.minimal_formula)
                    right_formula = str(self.right.minimal_formula)
                    result = f'({self.operator[0]} [' + left_formula + ' ' + 'U' + ' ' + right_formula + '] )'
                else:
                    left_formula = str(self.left.minimal_formula)
                    right_formula = str(self.right.minimal_formula)
                    result = '(' + left_formula + ' ' + self.operator + ' ' + right_formula + ')'

            self.minimal_formula = result

        else:
            self.minimal_formula = formula






    def isLeaf(self):
        return self.left == None and self.right == None and self.down == None

class PropositionNode(Node):
    def __init__(self, proposition_number, sub_tree_formula):
        super().__init__(sub_tree_formula = sub_tree_formula)
        self.proposition = Proposition(proposition_number)
        # self.formula = f'{{PROPOSITION {self.proposition.proposition_number}}}'
        self.formula = f'({self.proposition.proposition_number})'
        # self.sub_tree_formula = self.formula

    def __hash__(self):
        return hash(self.proposition)
        


class BooleanNode(Node):
    def __init__(self, bool_value : bool, sub_tree_formula):
        super().__init__(sub_tree_formula = sub_tree_formula)
        self.bool_value = bool_value
        # self.formula = '(True)' if bool_value == True else '(False)'
        # self.sub_tree_formula = self.formula

    def __hash__(self):
        if self.bool_value == True:
            return hash((HASH_TRUE, True))
        else:
            return hash((HASH_FALSE, False))

class OperatorNode(Node):
    def __init__(self, 
                 operator,
                 sub_tree_formula,
                 isTemporal : bool = False,
                 left = None,
                 right = None,
                 down = None,
                 ):
        """
        operator node must have atleast one child
        if binary, down should be None and 
        else then unary, left and right both should be None
        """
        assert((down != None and left == None and right == None) or (left != None and right != None and down == None))
        super().__init__(sub_tree_formula = sub_tree_formula)
        self.operator = operator
        self.isTemporal = isTemporal
        self.down = down
        self.left = left
        self.right = right
        self.formula = operator

        # if self.down != None:
        #     self.sub_tree_formula = '(' + self.formula + ' ' + self.down.sub_tree_formula + ')'
        # elif self.left != None and self.right != None:
        #     # first, let us not worry about EU
        #     self.sub_tree_formula = '(' + self.left.sub_tree_formula + ' ' + self.formula + ' ' + self.right.sub_tree_formula + ')'

    # assuming we don't need to hash this as of now, else hashing like((self.left, self.operator, self.right, self.down))
    # might lead to recursion ( a dfs of the nodes whenever we want to find the hash)

    # alternative is to store the hash value


    

















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
                 down = None
                 ):
        # self.value = value
        self.isBool = isBool
        self.isOperand = isOperand
        self.isOperator = isOperator
        self.isUnary = isUnary
        # left and right are for binary operators
        self.left = left
        self.right = right

        self.sub_tree_formula = ''

        # down is for unary operators
        self.down = down

        # denotes the sub formula that this node represents
        # self.sub_formula = ''
        #
        # sub_formula = ''
        # if self.down != None:
        #     sub_formula += value
        #     assert(isinstance(self.down, Node))
        #     sub_formula += self.down.sub_formula
        # else:
        #     if self.left != None:
        #         assert(isinstance(self.left, Node))
        #         sub_formula += self.left.sub_formula
        #     
        #     sub_formula += value
        #
        #     if self.right != None:
        #         assert(isinstance(self.right, Node))
        #         sub_formula += self.right.sub_formula
        #
        # self.sub_formula = sub_formula

    def isLeaf(self):
        return self.left == None and self.right == None and self.down == None


# class StateNode(Node):
#     def __init__(self, state_number : int):
#         super().__init__()
#         self.state = State(state_number)
#
#     def __hash__(self):
#         return hash(self.state)

class PropositionNode(Node):
    def __init__(self, proposition_number):
        super().__init__()
        self.proposition = Proposition(proposition_number)
        self.formula = f'{{PROPOSITION {self.proposition.proposition_number}}}'
        self.sub_tree_formula = self.formula

    def __hash__(self):
        return hash(self.proposition)
        


class BooleanNode(Node):
    def __init__(self, bool_value : bool):
        super().__init__()
        self.bool_value = bool_value
        self.formula = 'True' if bool_value == True else 'False'
        self.sub_tree_formula = self.formula

    def __hash__(self):
        if self.bool_value == True:
            return hash((HASH_TRUE, True))
        else:
            return hash((HASH_FALSE, False))

class OperatorNode(Node):
    def __init__(self, 
                 operator : str, 
                 isTemporal : bool = False,
                 left = None,
                 right = None,
                 down = None
                 ):
        """
        operator node must have atleast one child
        if unary, down should be None and 
        else then binary, left and right both should be None
        """
        assert((down != None and left == None and right == None) or (left != None and right != None and down == None))
        super().__init__()
        # have to convert to the ENUM
        self.operator = operator

        self.isTemporal = isTemporal
        self.down = down
        self.left = left
        self.right = right
        self.formula = operator

        if self.down != None:
            self.sub_tree_formula = self.formula + self.down.sub_tree_formula
        elif self.left != None and self.right != None:
            # first, let us not worry about EU
            self.sub_tree_formula = self.left.sub_tree_formula + self.formula + self.right.sub_tree_formula

    # assuming we don't need to hash this as of now, else hashing like((self.left, self.operator, self.right, self.down))
    # might lead to recursion ( a dfs of the nodes whenever we want to find the hash)

    # alternative is to store the hash value


    

















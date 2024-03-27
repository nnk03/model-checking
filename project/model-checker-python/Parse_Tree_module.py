"""
Class for Parser
"""
from Node_module import *
from Parser_module import parse_formula
from globals import *


class Parser():
    def __init__(self):
        # map is mapping from prop_variables to numbers
        self.map = {}
        # n represents total number of prop variables
        self.n = 0
        # track is tracking the number added to map
        self.track = 0
        self.check = ''

    def check_correctness(self, formula):
        self.check = ''
        formula = parse_formula(formula)
        tree = self.construct_parse_tree(formula)
        self.inorder_traversal(tree)
        print(self.check)

    def parse(self, formula):
        '''
        returns the parse tree
        '''
        formula_representation = parse_formula(formula)
        return self.construct_parse_tree(formula_representation)

    def construct_parse_tree(self, formula : tuple | str | bool):
        if isinstance(formula, tuple):
            # need to decide whether to use ENUM or STRING
            # print(formula)
            if formula[0] == 'EG':
                node = OperatorNode(
                    operator='EG',
                    isTemporal=True,
                    left = None,
                    right = None,
                    down = self.construct_parse_tree(formula[1])
                )
                return node
            elif formula[0] == 'EX':
                node = OperatorNode(
                    operator='EX',
                    isTemporal=True,
                    left = None,
                    right = None,
                    down = self.construct_parse_tree(formula[1])
                )
                return node
            elif formula[0] == 'EU':
                node = OperatorNode(
                    operator='EU',
                    isTemporal=True,
                    left = self.construct_parse_tree(formula[1]),
                    right = self.construct_parse_tree(formula[2]),
                    down = None
                )
                return node
            elif formula[0] == 'NOT':
                node = OperatorNode(
                    operator='NOT',
                    isTemporal=False,
                    left = None,
                    right = None,
                    down = self.construct_parse_tree(formula[1])
                )
                return node
            elif formula[0] == '&':
                node = OperatorNode(
                    operator='AND',
                    isTemporal=False,
                    left = self.construct_parse_tree(formula[1]),
                    right = self.construct_parse_tree(formula[2]),
                    down = None
                )
                return node
            elif formula[0] == '|':
                node = OperatorNode(
                    operator='OR', 
                    isTemporal=False,
                    left = self.construct_parse_tree(formula[1]),
                    right = self.construct_parse_tree(formula[2]),
                    down = None
                )
                return node
            elif formula[0] == 'IMPLIES':
                # this, if necessary, will implement *******************************************
                pass
            else:
                raise Exception('Unknown Operator')

        elif isinstance(formula, bool):
            node = BooleanNode(formula)
            return node

        elif isinstance(formula, str):
            prop_variable = formula
            if prop_variable in self.map:
                return PropositionNode(self.map[prop_variable])
            else:
                self.map[prop_variable] = self.track
                self.track += 1
                return PropositionNode(self.track - 1)

    
    def inorder_traversal(self, node):
        if node == None:
            return
        assert(isinstance(node, Node))

        if isinstance(node, OperatorNode):
            if node.down == None:
                self.inorder_traversal(node.left)
                # print(node.operator)
                self.check += node.operator + ' '
                self.inorder_traversal(node.right)
            else:
                self.check += node.operator + ' '
                # print(node.operator)
                self.inorder_traversal(node.down)


        elif isinstance(node, BooleanNode):
            self.check += str(node.bool_value) + ' '

        elif isinstance(node, PropositionNode):
            self.check += str(node.proposition.proposition_number) + ' '
        












"""
States are numbered from 0, ... , n - 1 where n is the number of states
Propositions are numbered from 0, ... , n - 1
Negation is represented as '-'
"""

from Closure_module import ClosureClass
from State_module import State
from Proposition_module import Proposition
from Node_module import *
from Parser_module import *


CLOSURE = ClosureClass()

# assuming we have a parse tree

class ModelChecker():
    def __init__(self):
        self.parser = Parser()

    def check_model(self, kripke_structure : list, formula : str):
        assert(
            isinstance(kripke_structure, list)
            and
            all([
                isinstance(element, State) for element in kripke_structure
            ])
            and
            isinstance(formula, str)
        )
        # assuming we have a parse tree

        tree = self.parser.construct_parse_tree(formula)

    def compute_closure(self, root : Node):
        # Node can be OperatorNode, BooleanNode or PropositionNode
        if isinstance(root, BooleanNode):
            pass

        elif isinstance(root, PropositionNode):
            pass

        elif isinstance(root, OperatorNode):
            pass




















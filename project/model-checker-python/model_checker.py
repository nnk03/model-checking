"""
States are numbered from 0, ... , n - 1 where n is the number of states
Propositions are numbered from 0, ... , n - 1
Negation is represented as '-'
"""

from Closure_module import ClosureClass
from State_module import State
from Proposition_module import Proposition
from Node_module import *
# from Parser_module import *
from Parse_Tree_module import Parser
from Kripke_Structure_module import *


# CLOSURE = ClosureClass()

# assuming we have a parse tree

class ModelChecker():
    def __init__(self, kripke_structure : Kripke_Structure):
        self.parser = Parser()
        assert(isinstance(kripke_structure, Kripke_Structure))
        self.kripke = kripke_structure
        self.closure = ClosureClass()

    def check_model(self, formula : str, state = None):
        assert(
            isinstance(formula, str)
        )
        tree = self.parser.return_parse_tree(formula)
        del self.closure
        self.closure = ClosureClass()

    def compute_closure(self, root : Node):
        assert(isinstance(root, Node))
        if root.sub_tree_formula in self.closure:
            # if already computed, no need to compute it again
            return

        # Node can be OperatorNode, BooleanNode or PropositionNode
        if isinstance(root, BooleanNode):
            if root.bool_value == True:
                # set of all states
                self.closure[root.sub_tree_formula] = self.kripke.states_set.copy()
            else:
                # empty set
                self.closure[root.sub_tree_formula] = set()


        elif isinstance(root, PropositionNode):
            proposition = root.proposition
            satisfying_states = set()
            assert(isinstance(proposition, Proposition))
            for state in self.kripke.states:
                # if proposition is present in the labelling
                # of the state, add the state
                if proposition in state.label_set:
                    satisfying_states.add(state)

            self.closure[root.sub_tree_formula] = satisfying_states


        elif isinstance(root, OperatorNode):

            if root.operator == 'AND':
                satisfying_states = set()
                left = root.left
                right = root.right
                assert(isinstance(left, Node) and isinstance(right, Node))
                self.compute_closure(left)
                self.compute_closure(right)

                left_sub_tree_formula = left.sub_tree_formula
                right_sub_tree_formula = right.sub_tree_formula

                closure_left = self.closure[left_sub_tree_formula]
                closure_right = self.closure[right_sub_tree_formula]
                for state in self.kripke.states:
                    # if a state is present in the closure of both left and right, add it 
                    if state in closure_left and state in closure_right:
                        satisfying_states.add(state)
                self.closure[root.sub_tree_formula] = satisfying_states

            elif root.operator == 'OR':
                satisfying_states = set()
                left = root.left
                right = root.right
                assert(isinstance(left, Node) and isinstance(right, Node))
                self.compute_closure(left)
                self.compute_closure(right)
                left_sub_tree_formula = left.sub_tree_formula
                right_sub_tree_formula = right.sub_tree_formula

                closure_left = self.closure[left_sub_tree_formula]
                closure_right = self.closure[right_sub_tree_formula]
                for state in self.kripke.states:
                    # if a state is present in the closure of both left and right, add it 
                    if state in closure_left or state in closure_right:
                        satisfying_states.add(state)
                self.closure[root.sub_tree_formula] = satisfying_states

            elif root.operator == 'NOT':
                satisfying_states = set()
                down = root.down
                assert(isinstance(down, Node))
                self.compute_closure(down)
                down_sub_tree_formula = down.sub_tree_formula
                closure_down = down_sub_tree_formula
                for state in self.kripke.states:
                    # if state does not satisfying phi, then it satisfies NOT phi
                    if state not in closure_down:
                        satisfying_states.add(state)

                self.closure[root.sub_tree_formula] = satisfying_states

            elif root.operator == 'EX':
                self.closure[root.sub_tree_formula] = self.return_closure_EX(root)

            elif root.operator == 'EG':
                self.closure[root.sub_tree_formula] = self.return_closure_EG(root)

            elif root.operator == 'EU':
                self.closure[root.sub_tree_formula] = self.return_closure_EU(root)

            else:
                raise Exception(f'{root.operator} IS AN UNKNOWN OPERATOR')

        else:
            raise Exception(f'UNKNOWN NODE TYPE')

    def return_closure_EU(self, root) -> set:
        assert(isinstance(root, OperatorNode))
        pass

    def return_closure_EX(self, root : OperatorNode) -> set:
        assert(isinstance(root, OperatorNode))
        satisfying_states = set()
        assert(isinstance(root, OperatorNode))
        sub_tree_formula = root.sub_tree_formula
        closure_sub_tree_formula = self.closure[sub_tree_formula]
        for state in self.kripke.states:
            # if there exist a successor satisfying the sub_tree_formula, add it
            assert(isinstance(state, State))
            for neighbour in state.next_states:
                # even if there is a self loop on this state, it is not a problem
                if neighbour in closure_sub_tree_formula:
                    satisfying_states.add(state)
                    break

        return satisfying_states

    def return_closure_EG(self, root) -> set:
        assert(isinstance(root, OperatorNode))
        pass



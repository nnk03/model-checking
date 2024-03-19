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
from Kripke_Structure_module import *


# CLOSURE = ClosureClass()

# assuming we have a parse tree

class ModelChecker():
    def __init__(self, kripke_structure : Kripke_Structure):
        self.parser = Parser()
        assert(isinstance(kripke_structure, Kripke_Structure))
        self.kripke = kripke_structure
        self.closure = None

    def check_model(self, formula : str):
        assert(
            isinstance(formula, str)
        )
        # assuming we have a parse tree

        tree = self.parser.construct_parse_tree(formula)
        del self.closure
        self.closure = ClosureClass()

    def compute_closure(self, root : Node):
        if root.sub_tree_formula in self.closure:
            # if already computed, no need to compute it again
            return

        # Node can be OperatorNode, BooleanNode or PropositionNode
        if isinstance(root, BooleanNode):
            if root.bool_value == True:
                # set of all states
                self.closure[root.sub_tree_formula] = self.kripke.states_set.copy()
            else:
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

            if root.operator == Operators.AND:
                satisfying_states = set()
                left = root.left
                right = root.right
                assert(isinstance(left, Node) and isinstance(right, Node))
                left_sub_tree_formula = left.sub_tree_formula
                right_sub_tree_formula = right.sub_tree_formula

                closure_left = self.closure[left_sub_tree_formula]
                closure_right = self.closure[right_sub_tree_formula]
                for state in self.kripke.states:
                    # if a state is present in the closure of both left and right, add it 
                    if state in closure_left and state in closure_right:
                        satisfying_states.add(state)
                self.closure[root.sub_tree_formula] = satisfying_states

            elif root.operator == Operators.OR:
                satisfying_states = set()
                left = root.left
                right = root.right
                assert(isinstance(left, Node) and isinstance(right, Node))
                left_sub_tree_formula = left.sub_tree_formula
                right_sub_tree_formula = right.sub_tree_formula

                closure_left = self.closure[left_sub_tree_formula]
                closure_right = self.closure[right_sub_tree_formula]
                for state in self.kripke.states:
                    # if a state is present in the closure of both left and right, add it 
                    if state in closure_left or state in closure_right:
                        satisfying_states.add(state)
                self.closure[root.sub_tree_formula] = satisfying_states

            elif root.operator == Operators.NOT:
                satisfying_states = set()
                down = root.down
                assert(isinstance(down, Node))
                down_sub_tree_formula = down.sub_tree_formula
                closure_down = down_sub_tree_formula
                for state in self.kripke.states:
                    # if state does not satisfying phi, then it satisfies NOT phi
                    if state not in closure_down:
                        satisfying_states.add(state)

                self.closure[root.sub_tree_formula] = satisfying_states

            elif root.operator == Operators.EX:
                self.closure[root.sub_tree_formula] = self.compute_closure_EX(root)

            elif root.operator == Operators.EG:
                self.closure[root.sub_tree_formula] = self.compute_closure_EG(root)

            elif root.operator == Operators.EF:
                self.closure[root.sub_tree_formula] = self.compute_closure_EF(root)

            else:
                raise f'{root.operator} IS AN UNKNOWN OPERATOR'

        else:
            raise f'UNKNOWN NODE TYPE'

    def compute_closure_EF(self) -> set:
        pass

    def compute_closure_EX(self, root : OperatorNode) -> set:
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

    def compute_closure_EG(self) -> set:
        pass



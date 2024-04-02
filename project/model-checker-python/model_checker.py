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

    def inorder_traversal(self, root : Node):
        if root == None:
            return
        self.inorder_traversal(root.left)
        print(root.sub_tree_formula)
        self.inorder_traversal(root.down)
        self.inorder_traversal(root.right)


    def check_model(self, formula : str, state = None):
        assert(
            isinstance(formula, str)
        )
        formula_representation = self.parser.parse(formula)
        print(formula_representation)
        # tree = self.parser.return_parse_tree(formula)
        tree = self.kripke.construct_parse_tree(formula_representation)
        # print(tree)
        # print('TREE INORDER TRAVERSAL')
        # self.inorder_traversal(tree)
        del self.closure
        self.closure = ClosureClass()
        self.compute_closure(tree)
        satisfying_states = self.closure[tree.sub_tree_formula]
        start_states_set = self.kripke.start_states_set
        if state == None:
            assert(isinstance(start_states_set, set))
            if start_states_set.issubset(satisfying_states):
                print('Formula Holds for all start states')
            else:
                print('Formula does not hold for all start states')

        ans = self.closure[tree.sub_tree_formula]
        print(ans)

    def compute_closure(self, root : Node):
        assert(isinstance(root, Node))
        # print('IN COMPUTE CLOSURE')
        # print(root.sub_tree_formula)
        # print(type(root))
        if root.sub_tree_formula in self.closure:
            # if already computed, no need to compute it again
            return

        # Node can be OperatorNode, BooleanNode or PropositionNode
        if isinstance(root, BooleanNode):
            if root.bool_value == True:
                # set of all states
                self.closure[root.sub_tree_formula] = self.kripke.copy_of_states_set()
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
                if proposition.proposition_number in state.label_set:
                    # print("HERE")
                    satisfying_states.add(state.state_number)

            # print('SATISFYING STATES OF')
            # print(root.sub_tree_formula)
            # print(satisfying_states)

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
                    if state.state_number in closure_left and state.state_number in closure_right:
                        satisfying_states.add(state.state_number)
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
                    if state.state_number in closure_left or state.state_number in closure_right:
                        satisfying_states.add(state.state_number)
                self.closure[root.sub_tree_formula] = satisfying_states

            elif root.operator == 'NOT':
                satisfying_states = set()
                down = root.down
                assert(isinstance(down, Node))
                self.compute_closure(down)
                down_sub_tree_formula = down.sub_tree_formula
                closure_down = self.closure[down_sub_tree_formula]
                for state in self.kripke.states:
                    # if state does not satisfying phi, then it satisfies NOT phi
                    if state.state_number not in closure_down:
                        satisfying_states.add(state.state_number)

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
        '''
        E[a U b] = b OR (a AND EX ( E [a U B] ))
        '''
        left = root.left
        right = root.right
        assert(isinstance(left, Node) and isinstance(right, Node))
        self.compute_closure(left)
        self.compute_closure(right)
        left_sub_tree_formula = left.sub_tree_formula
        right_sub_tree_formula = right.sub_tree_formula

        closure_left = self.closure[left_sub_tree_formula]
        closure_right = self.closure[right_sub_tree_formula]
        satisfying_states = set()
        # initially adding all states satisfying b
        for state in self.kripke.states:
            assert(isinstance(state, State))
            for neighbour in state.next_states:
                assert(isinstance(neighbour, State))
                if neighbour.state_number in closure_right:
                    satisfying_states.add(neighbour.state_number)

        # now for the 'repeat until step'
        curr = satisfying_states
        while True:
            prev = curr.copy()
            for state in self.kripke.states:
                assert(isinstance(state, State))
                if state.state_number in closure_left:
                    for neighbour in state.next_states:
                        assert(isinstance(neighbour, State))
                        if neighbour.state_number in closure_right:
                            curr.add(neighbour.state_number)
            if curr == prev:
                break

        satisfying_states = curr
        return satisfying_states

    def return_closure_EX(self, root : OperatorNode) -> set:
        assert(isinstance(root, OperatorNode))
        satisfying_states = set()
        assert(isinstance(root.down, Node))
        self.compute_closure(root.down)
        closure_down = self.closure[root.down.sub_tree_formula]
        for state in self.kripke.states:
            # if there exist a successor satisfying the sub_tree_formula, add it
            assert(isinstance(state, State))
            for neighbour in state.next_states:
                # even if there is a self loop on this state, it is not a problem
                assert(isinstance(neighbour, State))
                if neighbour.state_number in closure_down:
                    satisfying_states.add(state.state_number)
                    break

        return satisfying_states

    def return_closure_EG(self, root) -> set:
        assert(isinstance(root, OperatorNode))
        '''
        EG a = a AND EX EG a
        '''
        down = root.down
        assert(isinstance(down, Node))
        self.compute_closure(down)
        down_sub_tree_formula = down.sub_tree_formula

        closure_down = self.closure[down_sub_tree_formula]
        # print(closure_down)

        satisfying_states = set()
        # initially adding all states of kripke satisying 'a'
        for state in self.kripke.states:
            if state.state_number in closure_down:
                satisfying_states.add(state.state_number)

        # now for the 'repeat until step'
        curr = satisfying_states
        while True:
            prev = curr.copy()
            # print(curr)
            for state in self.kripke.states:
                if state.state_number in curr:
                    found = False
                    for neighbour in state.next_states:
                        assert(isinstance(neighbour, State))
                        if neighbour.state_number in curr:
                            found = True
                            break
                    if found == False and state.state_number in curr:
                        curr.remove(state.state_number)
            if curr == prev:
                break

        satisfying_states = curr
        # print(satisfying_states)
        return satisfying_states
        pass



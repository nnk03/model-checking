
from State_module import *
from Node_module import *


class Kripke_Structure():
    def __init__(self, n : int, m : int, prop_variables : list, start_states : list):
        self.n = n # number of states
        self.m = m # number of propositional variables
        self.states = [State(i) for i in range(n)]
        self.states_set = set(self.states)
        self.propositional_variables = [Proposition(i) for i in range(m)]
        self.start_state_numbers = start_states
        self.start_states_set = set(start_states)
        self.map_prop_variable_number = {}
        self.map_number_prop_variable = {}
        self.set_prop_variables(prop_variables)

    def copy_of_states_set(self):
        result = set()
        for state in self.states:
            result.add(state.state_number)
        return result

    def set_prop_variables(self, prop_variable : list):
        assert(len(prop_variable) == self.m)
        for i in range(self.m):
            # mapping propositional variable string to numbers
            self.map_prop_variable_number[prop_variable[i]] = i
            self.map_number_prop_variable[i] = prop_variable[i]



    def construct_parse_tree(self, formula : tuple | str | bool) -> Node:
        # print('In construct_parse_tree')
        # print(formula)
        if isinstance(formula, tuple):
            # decided to use string instead of ENUM for formula
            # print(formula)
            if formula[0] == 'EG':
                node = OperatorNode(
                    operator='EG',
                    isTemporal=True,
                    down = self.construct_parse_tree(formula[1]),
                    sub_tree_formula = formula,
                )
                return node
            elif formula[0] == 'EX':
                node = OperatorNode(
                    operator='EX',
                    isTemporal=True,
                    down = self.construct_parse_tree(formula[1]),
                    sub_tree_formula = formula,
                )
                # print('NODE')
                # print(node.sub_tree_formula)
                return node
            elif formula[0] == 'EU':
                node = OperatorNode(
                    operator='EU',
                    isTemporal=True,
                    left = self.construct_parse_tree(formula[1]),
                    right = self.construct_parse_tree(formula[2]),
                    sub_tree_formula = formula
                )
                return node
            elif formula[0] == 'NOT':
                node = OperatorNode(
                    operator='NOT',
                    isTemporal=False,
                    left = None,
                    right = None,
                    down = self.construct_parse_tree(formula[1]),
                    sub_tree_formula = formula
                )
                return node
            elif formula[0] == '&':
                node = OperatorNode(
                    operator='AND',
                    isTemporal=False,
                    left = self.construct_parse_tree(formula[1]),
                    right = self.construct_parse_tree(formula[2]),
                    down = None,
                    sub_tree_formula = formula
                )
                return node
            elif formula[0] == '|':
                node = OperatorNode(
                    operator='OR', 
                    isTemporal=False,
                    left = self.construct_parse_tree(formula[1]),
                    right = self.construct_parse_tree(formula[2]),
                    down = None,
                    sub_tree_formula = formula
                )
                return node
            # elif formula[0] == 'IMPLIES':
            # IMPLIES was not necessary as it is already converted to 
            # NOT p OR q in parser
            else:
                raise Exception(f'Unknown Operator {formula[0]}')

        elif isinstance(formula, bool):
            node = BooleanNode(formula, sub_tree_formula = formula)
            return node

        elif isinstance(formula, str):
            prop_variable = formula
            return PropositionNode(self.map_prop_variable_number[prop_variable], sub_tree_formula = formula)
            if prop_variable in self.map:
                return PropositionNode(self.map[prop_variable])
            else:
                self.map[prop_variable] = self.track
                prop_node = PropositionNode(self.track)
                self.track += 1
                return prop_node

    def set_label_for_state_i(self, i : int, labels : list):
        # label_numbers is a list of numbers corresponding to the proposition
        assert(
            isinstance(i, int)
            and
            isinstance(labels, list)
            and
            all([
                isinstance(ele, str) for ele in labels
            ])
        )
        labels = [
            self.map_prop_variable_number[val] for val in labels
        ]
        self.states[i].set_label(labels)

    def set_next_states_for_state_i(self, i : int, neighbour_numbers : list):
        # neighbour_numbers is a list of numbers corresponding to the neighbour States
        assert(
            isinstance(i, int)
            and
            isinstance(neighbour_numbers, list)
            and
            all([
                isinstance(ele, int) for ele in neighbour_numbers
            ])
        )
        neighbours = [
            self.states[val] for val in neighbour_numbers
        ]
        self.states[i].set_next_states(neighbours)

    def __str__(self):
        result = f'The Kripke structure is\n'
        for state in self.states:
            result += f'{state.state_number} : '
            for neighbour in state.next_states:
                result += f'{neighbour.state_number} '
            result += '\n'

        result += 'Labels are \n'
        for state in self.states:
            result += f'{state.state_number} : '
            for proposition_number in state.labels:
                result += f'{self.map_number_prop_variable[proposition_number]} '

            result += '\n'

        return result


        
















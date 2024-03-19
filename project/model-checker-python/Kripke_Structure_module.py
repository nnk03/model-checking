
from State_module import *


class Kripke_Structure():
    def __init__(self, n : int, m : int):
        self.n = n # number of states
        self.m = m # number of propositional variables
        self.states = [State(i) for i in range(n)]
        self.states_set = set(self.states)
        self.propositional_variables = [Proposition(i) for i in range(m)]

        
    def set_label_for_state_i(self, i : int, label_numbers : list):
        # label_numbers is a list of numbers corresponding to the proposition
        assert(
            isinstance(i, int)
            and
            isinstance(label_numbers, list)
            and
            all([
                isinstance(ele, int) for ele in label_numbers
            ])
        )
        labels = [
            self.propositional_variables[val] for val in label_numbers
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

        
















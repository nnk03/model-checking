"""
Class for states
"""
from globals import *

from Proposition_module import Proposition

class State():
    def __init__(self, state_number : int):
        assert(isinstance(state_number, int))
        self.state_number = state_number
        self.labels = []
        self.next_states = []
        # for fast lookups
        self.label_set = set()
        self.next_state_set = set()

    def set_label(self, labels : list):
        assert(
            isinstance(labels, list)
            and
            all([
                isinstance(element, Proposition) for element in labels
            ])
        )
        self.labels = labels
        self.label_set = set(labels)

    def set_next_states(self, neighbours : list):
        # neighbours is a list of States
        assert(
            isinstance(neighbours, list)
            and
            all([
                isinstance(element, State) for element in neighbours
            ])
        )
        self.next_states = neighbours
        # for fast lookups 
        self.next_state_set = set(neighbours)


    def __hash__(self) -> int:
        """
        Making it a tuple (0, state_number) in order to ensure 
        that state and propositions get different hash values
        as propositions will be hashed as 
        (1, proposition_number)
        """
        return hash((STATE_HASH, self.state_number))

    def __str__(self):
        res = f'{{STATE {self.state_number}}}'
        return res

    
# d = {}
# for i in range(5):
#     d[State(i)] = i
#
# for a, b in d.items():
#     print(a, b)














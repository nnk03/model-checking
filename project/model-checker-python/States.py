"""
Class for states
"""
STATE_HASH = 0

class State():
    def __init__(self, state_number : int):
        assert(isinstance(state_number, int))
        self.state = state_number

    def __hash__(self) -> int:
        """
        Making it a tuple (0, state_number) in order to ensure 
        that state and propositions get different hash values
        as propositions will be hashed as 
        (1, proposition_number)
        """
        return hash((STATE_HASH, self.state))

    def __str__(self):
        res = f'{{STATE {self.state}}}'
        return res

    
d = {}
for i in range(5):
    d[State(i)] = i

for a, b in d.items():
    print(a, b)














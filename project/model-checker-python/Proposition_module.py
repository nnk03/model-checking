"""
Class for propositions
"""
from globals import *

class Proposition():
    def __init__(self, proposition_number : int):
        assert(isinstance(proposition_number, int))
        self.proposition_number = proposition_number

    def __hash__(self) -> int:
        """
        Making it a tuple (1, proposition_number) in order to ensure 
        that propositions and states get different hash values
        as states will be hashed as 
        (0, state_number)
        """
        return hash((PROPOSITION_HASH, self.proposition_number))
    
    def __str__(self):
        res = f'{{PROPOSITION {self.proposition_number}}}'
        return res
















"""
CLOSURE(formula) is the set of states satisfying the formula
"""

# dictionary to store the formula and the set of states satisfying the formula
class ClosureClass(dict):
    def __getitem__(self, key):
        try:
            res = super().__getitem__(key)
            return res
        except:
            return None
    
    def __setitem__(self, key, value):
        super().__setitem__(key, value)


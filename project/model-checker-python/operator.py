# allowed operators
from enum import Enum

class Operator(Enum):
    OR = 'v'
    AND = '^'
    IMPLIES = '>'
    X = 'X'
    AF = 'AF'
    EF = 'EF'
    AG = 'AG'
    EG = 'EG'
    AU = 'AU'
    EU = 'EU'

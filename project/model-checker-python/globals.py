STATE_HASH = 0
PROPOSITION_HASH = 1
HASH_TRUE = 2
HASH_FALSE = 3
HASH_OPERATOR_NODE = 4

from enum import Enum, auto
class Operators(Enum):
    EF = auto()
    EX = auto()
    EG = auto()
    EU = auto()
    AND = auto()
    OR = auto()
    NOT = auto()


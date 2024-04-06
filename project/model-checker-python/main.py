# This is the main function
# import sys
# n = len(sys.argv)
#
# flag = None if n == 1 else sys.argv[1]

from Kripke_Structure_module import Kripke_Structure
from model_checker import ModelChecker


n = int(input('Enter number of states\n'))
m = int(input('Enter number of propositional variables\n'))

lst_prop_variables = input('Enter the propositional variables delimited by space\n').split()

start_states = list(map(int, input('Enter the start states delimited by space\n').split()))

k = Kripke_Structure(n, m, lst_prop_variables, start_states)

for i in range(n):
    print(f'Enter the next states of state {i} delimited by space')
    neighbours = list(map(int, input().split()))
    k.set_next_states_for_state_i(i, neighbours)

for i in range(n):
    print(f'Enter the labels for state {i} delimited by space (DON\'T PUT THE NEGATIONS OF PROPOSITIONAL VARIABLES)')
    labels = list(input().split())
    k.set_label_for_state_i(i, labels)

print(k)

m = ModelChecker(k)
print()

while True:
    try:
        formula = input()
        m.check_model(formula)
        print()
    except EOFError:
        break









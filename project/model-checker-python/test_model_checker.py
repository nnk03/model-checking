from Kripke_Structure_module import Kripke_Structure
from model_checker import ModelChecker



k = Kripke_Structure(3, 2, ['p', 'q'], [0])

s1 = k.states[0]
s2 = k.states[1]
s3 = k.states[2]

p = k.propositional_variables[0]
q = k.propositional_variables[1]

# proposition numbers
P = 0
Q = 1

# State Numbers
A = 0
B = 1
C = 2

k.set_prop_variables(['p', 'q'])

k.set_label_for_state_i(A, ['p', 'q'])
k.set_label_for_state_i(B, ['q'])
k.set_label_for_state_i(C, ['p'])

k.set_next_states_for_state_i(A, [B])
k.set_next_states_for_state_i(B, [A, C])
k.set_next_states_for_state_i(C, [C])

print(k)

m = ModelChecker(k)

while True:
    formula = input()
    m.check_model(formula)
    print()
















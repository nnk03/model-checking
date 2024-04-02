from Kripke_Structure_module import Kripke_Structure
from model_checker import ModelChecker



k = Kripke_Structure(3, 2)

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

k.set_label_for_state_i(A, [P, Q])
k.set_label_for_state_i(B, [Q])
k.set_label_for_state_i(C, [P])

k.set_next_states_for_state_i(A, [B])
k.set_next_states_for_state_i(B, [A, C])
k.set_next_states_for_state_i(C, [C])

print(k)

m = ModelChecker(k)

m.check_model('p')















# This is the main function
# import sys
# n = len(sys.argv)
#
# flag = None if n == 1 else sys.argv[1]

from Kripke_Structure_module import Kripke_Structure
from model_checker import ModelChecker

file_name = input('Enter file\n')
with open(file_name, 'r') as file:
    file_content = file.readlines()
    for i in range(len(file_content)):
        file_content[i] = file_content[i].replace('\n', '')

    print(file_content)

    
    i = 0
    n = int(file_content[i])  # number of states
    # print(n)
    i += 1

    m = int(file_content[i])  # number of prop variables
    # print(m)
    i += 1

    lst_prop_variables = file_content[i].split()
    # print(lst_prop_variables)
    i += 1

    start_states = list(map(int, file_content[i].split()))
    # print(start_states)
    i += 1

    k = Kripke_Structure(n, m, lst_prop_variables, start_states)

    for state_num in range(n):
        # next states
        neighbours = list(map(int, file_content[i].split()))
        k.set_next_states_for_state_i(state_num, neighbours)
        i += 1

    for state_num in range(n):
        # labels of states
        labels = list(file_content[i].split())
        k.set_label_for_state_i(state_num, labels)
        i += 1

    print(k)
    m = ModelChecker(k)
    print()

    for j in range(i, len(file_content)):
        formula = file_content[j]
        formula = formula.strip()
        if formula != '':
            m.check_model(formula)
            print('*' * 100)
        print()













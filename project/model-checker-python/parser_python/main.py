from parser import parse_formula


with open('./testcases', 'r') as file:
    lst = file.readlines()
    print(lst)
    for i in range(len(lst)):
        lst[i] = lst[i].replace('\n', '')
    for row in lst:
        if row != '':
            print(parse_formula(row))






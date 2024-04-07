# from Parse_Tree_module import Parser
#
# formula = input('Enter formula ')
# parser = Parser()
# parser.check_correctness(formula)

class A(dict):
    def __init__(self):
        super().__init__()


a = A()
a[3] = 4
print(3 in a)







# from enum import Enum, auto
#
# class Color(Enum):
#     RED = auto()
#     BLUE = auto()
#     DF = auto()
#
# for color in Color:
#     print(color.name)

#
#
# class Test(dict):
#     def __getitem__(self, key):
#         return super().__getitem__(key)
#
#     def __setitem__(self, key, value):
#         super().__setitem__(key, value)
#
#
# t = Test()
# t[2] = 3
# t[4] = 124
#
# t1 = Test()
# t1[2] = 1234
# t1[3] = 2345678
#
# for a, b in t.items():
#     print(a, b)
#
# for a, b in t1.items():
#     print(a, b)
#
#
#
#
#
#
#

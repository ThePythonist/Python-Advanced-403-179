from pprint import pprint


# def func(*args):
#     # args = list(args)
#     print(args)
#
#
# func(10, 20, 30, 40)


# def func(**kwargs):
#     # print(kwargs)
#
#     for i in kwargs.items():
#         print(i)
#
#     # v = tuple(kwargs.values())
#     # k = tuple(kwargs.keys())
#     # print(k)
#     # print(v)
#
#
# func(name="kamiar", age=24, job="barista", city="tehran")

def func(**kwargs):
    pprint(kwargs,sort_dicts=False)


students = ["amirali", "amirali", "parham", "shayan", "parsa", "farbod"]
func(teacher="sadeghi", students=students, level="advanced")

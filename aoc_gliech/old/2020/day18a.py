from aocd import get_data
from operator import add, mul, methodcaller

op_dict = {"+": add, "*": mul}

def calc(expr):
    a = expr.pop()
    if a == ")":
        a = calc(expr)
    else:
        a = int(a)
    if len(expr) == 0:
        return a
    op = expr.pop()
    if op == "(":
        return a
    else:
        op = op_dict[op]
    b = calc(expr)
    return op(a, b)

data = get_data(year=2020, day=18).split("\n")
data = map(methodcaller("replace", " ", ""), data)
data = map(list, data)
data = map(calc, data)
print(sum(data))

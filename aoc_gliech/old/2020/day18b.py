from aocd import get_data
from operator import add, mul, methodcaller
from functools import reduce

def calc_without_paranthesis(expr):
    expr_without_add = [int(expr[0])]
    for idx, num in enumerate(expr[2::2]):
        num = int(num)
        if expr[idx*2+1] == "+":
            expr_without_add[-1] += num
        else:
            expr_without_add.append(num)
    return(reduce(mul, expr_without_add))

def calc(expr):
    expr.reverse()
    expr_without_paranthesis = []
    while expr != []:
        char = expr.pop()
        if char == "(":
            inner_expr = []
            lvl = 0
            while (inner_char:=expr.pop()) != ")" or lvl > 0:
                if inner_char == "(":
                    lvl += 1
                elif inner_char == ")":
                    lvl -= 1
                inner_expr.append(inner_char)
            char = calc(inner_expr)
        expr_without_paranthesis.append(char)
    return calc_without_paranthesis(expr_without_paranthesis)

data = get_data(year=2020, day=18).split("\n")
data = map(methodcaller("replace", " ", ""), data)
data = map(list, data)
data = map(calc, data)
print(sum(data))

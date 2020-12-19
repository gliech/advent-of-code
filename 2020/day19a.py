from aocd import get_data
import re

def expand_rule(rule_id):
    rule = rules[rule_id]
    encase = '|' in rule
    expanded_rule = []
    for cell in rule:
        if type(cell) == int:
            expanded_rule += expand_rule(cell)
        else:
            expanded_rule.append(cell)
    if encase:
        expanded_rule = ['('] + expanded_rule + [')']
    return expanded_rule

data = get_data(year=2020, day=19)
# data = """0: 4 1 5
# 1: 2 3 | 3 2
# 2: 4 4 | 5 5
# 3: 4 5 | 5 4
# 4: "a"
# 5: "b"
#
# ababbb
# bababa
# abbbab
# aaabbb
# aaaabbb"""
rules, messages = data.split('\n\n')
rules = rules.replace('"', '').split('\n')
rules = {int((r:=rule.split(':'))[0]): [int(c) if c.isnumeric() else c for c in r[1].split()] for rule in rules}
rule = re.compile(r''.join(expand_rule(0)))

messages = messages.split('\n')
messages = filter(lambda a: bool(re.fullmatch(rule, a)), messages)
messages = list(messages)

print(len(messages))

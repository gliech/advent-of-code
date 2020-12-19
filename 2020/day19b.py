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
rules, messages = data.split('\n\n')
rules = rules.replace('"', '').split('\n')
rules = {int((r:=rule.split(':'))[0]): [int(c) if c.isnumeric() else c for c in r[1].split()] for rule in rules}
rules[8] = [42,'+']
valid_messages = set()
messages = messages.split('\n')

#this feels dirty V
for i in range(1,20):
    rules[11] = [42,f'{{{i}}}',31,f'{{{i}}}']
    rule = re.compile(r''.join(expand_rule(0)))
    valid_messages.update(filter(lambda a: bool(re.fullmatch(rule, a)), messages))

print(len(valid_messages))

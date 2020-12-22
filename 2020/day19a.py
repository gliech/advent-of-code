from aocd import get_data
import re

def expand_rule(rule_id):
    rule = rules[rule_id]
    encase = '|' in rule
    expanded_rule = []
    for cell in rule:
        if cell.isnumeric():
            expanded_rule += expand_rule(cell)
        else:
            expanded_rule.append(cell)
    if encase:
        expanded_rule = ['('] + expanded_rule + [')']
    return expanded_rule

rules, messages = get_data(year=2020, day=19).split('\n\n')

rules = rules.replace('"', '').split('\n')
rules = {(r:=rule.split(':'))[0]: r[1].split() for rule in rules}
rule = re.compile(r''.join(expand_rule('0')))

messages = messages.split('\n')
messages = filter(lambda a: bool(re.fullmatch(rule, a)), messages)
messages = list(messages)

print(len(messages))

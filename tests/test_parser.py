import dill

from src.Parser.Parser import format_rules
from src.Parser.FiniteAutomaton.FiniteAutomaton import build_dfa

rules = {
    'stat': [
        ('ifS', lambda x: x)
    ],
    'ifS': [
        ('if stat else stat', lambda x, y, z, w: x)
    ]
}

formatted_rules = format_rules(rules)

with open('test.p', "wb") as file:
    dill.dump(formatted_rules, file)

with open('test.p', "rb") as file:
    formatted_rules = dill.load(file)

print(formatted_rules)

dfa = build_dfa(formatted_rules, ["stat"])

print(dfa)
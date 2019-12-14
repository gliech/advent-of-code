# Setup
from aocd import get_data
from operator import methodcaller
aoc_data = get_data(year=2019, day=14).split('\n')

class resource:
    def __init__(self, output_volume, **kwargs):
        self.stash = 0
        self.output_volume = output_volume
        self.input_requirements = kwargs

    def consume(self, amount):
        while self.stash < amount:
            self.produce()
        self.stash -= amount

    def produce(self):
        for resource, amount in self.input_requirements.items():
            resources[resource].consume(amount)
        self.stash+=self.output_volume

class ore:
    def __init__(self):
        self.consumed = 0

    def consume(self, amount):
        self.consumed += amount

resources = {'ORE': ore()}

for recipe in aoc_data:
    raw_reqs, raw_output = recipe.split(' => ')
    output_volume, resource_name = raw_output.split()
    raw_ingredients = map(methodcaller('split'),raw_reqs.split(','))
    input_reqs = {ingr[1]: int(ingr[0]) for ingr in raw_ingredients}
    resources[resource_name] = resource(int(output_volume), **input_reqs)

resources['FUEL'].consume(1)
print(resources['ORE'].consumed)

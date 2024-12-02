# Setup
from aocd import get_data
from operator import methodcaller
from math import ceil
aoc_data = get_data(year=2019, day=14).split('\n')

class resource:
    def __init__(self, output_volume, **kwargs):
        self.stash = 0
        self.output_volume = output_volume
        self.input_requirements = kwargs

    def consume(self, amount=1):
        if self.stash < amount:
            self.produce(amount-self.stash)
        self.stash -= amount

    def produce(self, pieces):
        recipes = ceil(pieces/self.output_volume)
        for resource, amount in self.input_requirements.items():
            resources[resource].consume(amount*recipes)
        self.stash+=self.output_volume*recipes

    def reset(self):
        self.stash = 0

class ore:
    def __init__(self):
        self.stash = int(1e12)

    def consume(self, amount):
        self.stash -= amount

    def reset(self):
        self.stash = int(1e12)


resources = {'ORE': ore()}

for recipe in aoc_data:
    raw_reqs, raw_output = recipe.split(' => ')
    output_volume, resource_name = raw_output.split()
    raw_ingredients = map(methodcaller('split'),raw_reqs.split(','))
    input_reqs = {ingr[1]: int(ingr[0]) for ingr in raw_ingredients}
    resources[resource_name] = resource(int(output_volume), **input_reqs)

def ore_required(fuel):
    for resource in resources.values():
        resource.reset()
    resources['FUEL'].consume(fuel)
    return resources['ORE'].stash

low = 1
high = int(1e12)
while high-low>1:
    test=low+(high-low)//2
    test_result=ore_required(test)
    if test_result<0:
        high=test
    else:
        low=test
    print(f'{test}: {test_result}')

print(f'Fuel for 1 Trillion ore: {low} ({ore_required(low)} ore left over)')

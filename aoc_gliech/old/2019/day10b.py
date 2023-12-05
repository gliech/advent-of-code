# Setup
from aocd import get_data
from cmath import phase, pi
from collections import defaultdict
aoc_data = get_data(year=2019, day=10).split('\n')

example = '''.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##'''.split('\n')

# Longform
def long_solution(data):
    def coords(pic):
        for y, row in enumerate(pic):
            for x, pixel in enumerate(row):
                if pixel=='#':
                    yield complex(x,y)

    def translate(origin,cloud):
        return{x-origin for x in cloud if x!=origin}

    def visible(cloud):
        asteroids_by_direction = defaultdict(lambda: set())
        for asteroid in cloud:
            asteroids_by_direction[phase(asteroid)].add(asteroid)
        return [min(x,key=abs) for x in asteroids_by_direction.values()]

    def positive_angle(number):
        angle = phase(number)+pi/2
        if angle >= 0:
            return angle
        else:
            return 2*pi+angle

    def lazor(cloud):
        while len(cloud)>0:
            visible_asteroids=sorted(visible(cloud),key=positive_angle)
            for asteroid in visible_asteroids:
                yield asteroid
                cloud.remove(asteroid)

    cloud = set(coords(data))
    station_location = max(cloud,key=lambda x: len(visible(translate(x,cloud))))
    cloud_at_station = translate(station_location, cloud)
    bet = list(lazor(cloud_at_station))[199]
    rev_translated_bet = bet+station_location
    return(rev_translated_bet.real*100+rev_translated_bet.imag)

# Golfed
def golfed_solution(d):
    return d

# Output
solve=0
print([long_solution, golfed_solution][solve](aoc_data))

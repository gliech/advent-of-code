# Setup
from aocd import data
from datetime import datetime
from re import match
from collections import defaultdict, Counter
from itertools import chain
d={ datetime.strptime(time, '%Y-%m-%d %H:%M'): True if event == 'falls asleep' else False if event == 'wakes up' else int(match(r'.*#(\d+) .*', event).group(1)) for time, event in ( match(r'\[(.+)\] (.+)', entry).groups() for entry in data.split('\n') ) }

# Longform
naps_per_guard = defaultdict(list)
for time, event in sorted(d.items()):
    if type(event) is int:
        guard = event
    elif event:
        start = time
    else:
        naps_per_guard[guard].append( (start.minute, time.minute) )
total_naptime_per_guard = { guard: sum( b-a for a,b in naps ) for guard, naps in naps_per_guard.items() }
sleepiest_guard = max(total_naptime_per_guard, key=total_naptime_per_guard.get)
a = Counter( chain( *( range(start,end) for start, end in naps_per_guard[sleepiest_guard] ) ) ).most_common(1)[0][0] * sleepiest_guard
# Golfed

# Output
print(a)

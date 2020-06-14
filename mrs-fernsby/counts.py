#!/usr/bin/env python3
from collections import defaultdict

# Read in the data
with open('d8184e350cc288c4533ba1ceff32531b', 'r') as f:
    s = f.read()

# Count the number of each unique character
counts = defaultdict(int)
for c in s:
    counts[c] += 1

for c, count in counts.items():
    print(c, count)
print(len(counts))

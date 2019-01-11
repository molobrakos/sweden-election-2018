#!/usr/bin/env python3

from itertools import chain, combinations

# https://data.val.se/val/val2018/slutresultat/R/rike/valda.html
SEATS=dict(
    S=100,
    M=70,
    SD=62,
    C=31,
    V=28,
    KD=22,
    L=20,
    MP=16)

PARTIES = SEATS.keys()
TOTAL_SEATS = sum(SEATS.values())
MAJORITY = TOTAL_SEATS / 2

assert(TOTAL_SEATS == 349)

def has_majority(c):
    return sum(SEATS[p] for p in c) > MAJORITY


def powerset(s):
    # https://docs.python.org/3.4/library/itertools.html
    return chain.from_iterable(combinations(s, r)
                               for r in range(len(s)+1))


candidates = list(powerset(PARTIES))
assert(len(candidates) == 1<<len(PARTIES))  # 8 parties, 256 constellations (including empty constellation)

#  only keep constellations with majority (also excluding empty constellation)
candidates = (c for c in candidates
              if has_majority(c))

MUTUAL_EXCLUSIVES = [
    ("SD", "S"),
    ("SD", "L"),
    ("SD", "V"),
    ("SD", "MP"),
    ("SD", "C"),
    ("V", "M"),
    ("KD", "V"),
    ("S", "M"),
    ("S", "KD"),
    ("L", "V"),
]

def mutual_exclusives(c):
    return any(a in c and
               b in c
               for a, b in MUTUAL_EXCLUSIVES)

candidates = [c for c in candidates
              if not mutual_exclusives(c)]

from pprint import pprint
pprint(candidates)
print(len(candidates))

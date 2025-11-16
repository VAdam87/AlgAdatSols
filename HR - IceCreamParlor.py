# https://www.hackerrank.com/challenges/icecream-parlor/problem?isFullScreen=true
# Kereses

def icecreamParlor(m, arr):
    d = {}
    for i, cost in enumerate(arr):
        if m - cost in d:
            return sorted([i + 1, d[m - cost] + 1])
        else:
            d[cost] = i
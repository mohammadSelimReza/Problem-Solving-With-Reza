"""
Fast I/O template for competitive programming.
Handles large input efficiently with sys.stdin.
"""
import sys
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from bisect import bisect_left, bisect_right
from math import gcd, ceil, floor, log2, inf
from functools import lru_cache
from itertools import permutations, combinations, accumulate

input = sys.stdin.readline
print = sys.stdout.write


def inp():
    """Read a single integer."""
    return int(input())


def inlt():
    """Read a list of integers."""
    return list(map(int, input().split()))


def insr():
    """Read a string."""
    return input().strip()


def invr():
    """Read space-separated integers as separate variables."""
    return map(int, input().split())


def solve():
    pass


def main():
    t = inp()
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()

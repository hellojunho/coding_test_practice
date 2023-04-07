import sys

n, k = map(int, sys.stdin.readline().split())

_n = 1
for i in range(k):
    _n *= (n-i)

_k = 1
for i in range(1, k+1):
    _k *= i

print(round(_n/_k))
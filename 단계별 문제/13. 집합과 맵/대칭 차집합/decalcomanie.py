import sys

input = sys.stdin.readline

n, m = map(int, input().split())

setA = set(list(map(int, input().split())))
setB = set(list(map(int, input().split())))

del1 = len(set(setA) - set(setB))
del2 = len(set(setB) - set(setA))

print(del1 + del2)
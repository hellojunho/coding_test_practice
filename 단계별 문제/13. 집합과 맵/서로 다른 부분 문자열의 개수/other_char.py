import sys

input = sys.stdin.readline

n = input().rstrip()

s = set()
for i in range(len(n)):
    for j in range(i, len(n)):
        s.add(n[i:j+1])

print(len(s))